import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client (NEW SDK)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_best_model():
    try:
        models = list(client.models.list())
        for m in models:
            if "flash" in m.name.lower() and "generateContent" in m.supported_actions:
                return m.name
    except Exception:
        pass
    return "gemini-1.5-flash"

ACTIVE_MODEL = get_best_model()

def get_gemini_response(user_query, live_context):
    prompt = f"""
You are an ApexEdge Agent, a helpful and versatile assistant.

INSTRUCTIONS:
1. You have access to a real-time knowledge base provided in the "CONTEXT" section below.
2. ALWAYS prioritize information from the CONTEXT.
3. If the answer is found in the CONTEXT, cite the specific file or source if possible.
4. If the answer is NOT in the CONTEXT, use your own general knowledge to answer helpfuly.
5. Do NOT say "I cannot answer this because it's not in the context" unless it is a query about a specific private record that you legitimately don't have.

CONTEXT:
{live_context}

QUESTION:
{user_query}
"""
    try:
        response = client.models.generate_content(
            model=ACTIVE_MODEL,
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def get_image_description(image_bytes: bytes) -> str:
    """
    Sends an image to Gemini to get a description/transcription.
    """
    prompt = "Analyze this image. Transcribe any text you see and describe the key visual elements."
    try:
        from PIL import Image
        import io
        
        image = Image.open(io.BytesIO(image_bytes))
        
        response = client.models.generate_content(
            model=ACTIVE_MODEL,
            contents=[prompt, image]
        )
        return f"[Image Analysis]: {response.text}"
    except Exception as e:
        return f"[Error analyzing image: {str(e)}]"
