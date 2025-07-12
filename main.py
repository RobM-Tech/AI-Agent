import sys
from agent import run_agent

def main():
    args = sys.argv[1:]
    verbose = "--verbose" in args #verbose is now True or False
    args = [word for word in args if word != "--verbose"]

    user_prompt = " ".join(args)
    if not user_prompt:
        print("No prompt provided.")
        exit(1)

    text, prompt_tokens, response_tokens = run_agent(user_prompt)

    

    if verbose:
        print(f"""\n
        User prompt: {user_prompt}
        Prompt tokens: {prompt_tokens}
        Response tokens: {response_tokens}
        """)
    else:
        print({text})
    
if __name__ == "__main__":
    main()