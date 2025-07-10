import os, sys
from dotenv import load_dotenv
from google import genai

# Load .env file and get the Gemini API key
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
)

prompt_token_count = response.usage_metadata.prompt_token_count
candidates_token_count = response.usage_metadata.candidates_token_count


def main():
    user_prompt = " ".join(sys.argv[1:])
    if user_prompt == "":
        exit(1)

    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents={user_prompt})

    prompt_token_count = response.usage_metadata.prompt_token_count
    candidates_token_count = response.usage_metadata.candidates_token_count


    print(f"""\
    {response.text}\n 
    Prompt tokens: {prompt_token_count}\n 
    Response tokens: {candidates_token_count}""")
    

if __name__ == "__main__":
    main()