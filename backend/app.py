import os
import pathway as pw
from fastapi import FastAPI, Request
from agent import get_gemini_response
from gemini_index import start_pathway_pipeline

app = FastAPI(title="Synaptix Pathway Agent")

# 1. Initialize Pathway Streaming Table
table = start_pathway_pipeline("./data")

@app.post("/ask")
async def ask_endpoint(request: Request):
    data = await request.json()
    query = data.get("query", "")

    # 2. Fetch current context from Pathway
    # In a simple setup, we reduce the table to a single string of all content
    # For production, you'd use Pathway's Vector Index here.
    content_list = pw.debug.table_to_list(table)
    live_context = "\n---\n".join([row['data'] for row in content_list])
    
    print(f"🔔 Pathway context updated. Size: {len(live_context)} chars")
    
    answer = get_gemini_response(query, live_context)
    return {"answer": answer}

if __name__ == "__main__":
    # 3. Start Pathway and Uvicorn
    # Note: pw.run() is blocking, so in a real app you'd run the 
    # pipeline in the background or use Pathway's built-in connectors.
    import uvicorn
    import threading

    # Run Pathway in a background thread
    threading.Thread(target=pw.run, daemon=True).start()
    
    uvicorn.run(app, host="0.0.0.0", port=8000)