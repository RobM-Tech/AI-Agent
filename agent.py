import sys
from gemini_client import client
from google.genai import types # type: ignore

def run_agent(user_prompt: str):
    if not user_prompt:
        raise ValueError("Prompt cannot be empty.")
    
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]   

    response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    )

    prompt_token_count = response.usage_metadata.prompt_token_count
    candidates_token_count = response.usage_metadata.candidates_token_count

    return response.text, prompt_token_count, candidates_token_count