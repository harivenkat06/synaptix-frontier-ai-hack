import os
import shutil
import pathway as pw
from fastapi import FastAPI, Request, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from agent import get_gemini_response
from gemini_index import start_pathway_pipeline

app = FastAPI(title="Synaptix Pathway Agent")

# Add CORS middleware for development (allow all origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Pathway streaming pipeline (watch ./data directory)
# This returns a dictionary that updates in real-time
context_store = start_pathway_pipeline("./data")

@app.post("/upload")
async def upload_file(files: list[UploadFile] = File(...)):
    try:
        if not os.path.exists("./data"):
            os.makedirs("./data")
        
        saved_files = []
        for file in files:
            file_path = f"./data/{file.filename}"
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            saved_files.append(file.filename)
            
        return {"filenames": saved_files, "message": f"Successfully uploaded {len(saved_files)} file(s). Indexing started."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask")
async def ask_endpoint(request: Request):
    """Handle a query from the frontend.
    Accepts JSON payloads of the form {"query": "..."} or a raw string.
    """
    data = await request.json()
    if isinstance(data, dict):
        query = data.get("query", "")
    else:
        query = str(data)

    # Retrieve current context from the global store populated by Pathway
    # We join all available file contents into one context string.
    if context_store:
        live_context = "\n---\n".join(context_store.values())
    else:
        live_context = "No context data available."
        
    print(f"🔔 Pathway context updated. Size: {len(live_context)} chars")

    answer = get_gemini_response(query, live_context)
    return {"answer": answer}

if __name__ == "__main__":
    # Run Pathway in a background thread
    import threading
    threading.Thread(target=pw.run, daemon=True).start()
    # Use a non‑conflicting port (8001) to avoid "address already in use"
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
