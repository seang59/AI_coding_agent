import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
import prompts
import call_function


def main():
    load_dotenv()
    function_results = []

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Chatbot using Gemini API")
    parser.add_argument("user_prompt", type=str, help="The prompt to send to Gemini")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Construct messages list
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]


    # Load API key from environment variable
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    print("API key loaded")
    client = genai.Client(api_key=api_key)

    for i in range(20): 
        # Generate content, contents = prompt
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=messages, 
            config=types.GenerateContentConfig(
                tools=[call_function.available_functions],
                system_instruction=prompts.SYSTEM_PROMPT,
            )   
        )

        # Print token usage metadata if verbose is enabled
        usage_metadata = response.usage_metadata

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)
        
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {usage_metadata.prompt_token_count}")
            print(f"Response tokens: {usage_metadata.candidates_token_count}")

        # Print the generated text or function calls
        if response.function_calls:
            for func_call in response.function_calls:
                result = call_function.call_function(func_call, verbose=args.verbose)
                if not result.parts:
                    raise Exception("No parts returned from function call.")
                
                first_part = result.parts[0]

                if not first_part.function_response:
                    raise Exception("No response in the function call result.")
                if  first_part.function_response.response is None:
                    raise Exception("No sub-parts in the function call result.")

                function_results.append(first_part)
                messages.append(types.Content(role="user", parts=function_results))

                if args.verbose:
                    print(f"-> {result.parts[0].function_response.response}")
        else:
            print(response.text)
            break

        if i == 19:
            print("Reached maximum iterations without a final response.")
            exit(1)

        

if __name__ == "__main__":
    main()
