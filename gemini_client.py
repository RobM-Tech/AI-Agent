import os
from dotenv import load_dotenv
from google import genai

# Load .env file and get the Gemini API key
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

client = genai.Client(api_key=api_key)