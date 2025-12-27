import os
from google import genai
from dotenv import load_dotenv  # <-- Add this

# Load the .env file from the current directory
load_dotenv() 

# Now os.getenv will actually find your key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Use environment variables for security
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_best_model():
    try:
        available_models = list(client.models.list())
        for m in available_models:
            if "flash" in m.name.lower() and "generateContent" in m.supported_actions:
                return m.name
    except Exception:
        pass
    return "gemini-1.5-flash"

ACTIVE_MODEL = get_best_model()

def get_gemini_response(user_query, live_context):
    prompt = f"You are a Synaptix Agent.\nCONTEXT: {live_context}\nQUESTION: {user_query}"
    try:
        response = client.models.generate_content(model=ACTIVE_MODEL, contents=prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"