
from gemini_api import ask_gemini
from tokenizer import tokenize_text, print_colored_tokens, print_token_details


def main():

    print("Custom Tokenizer + Gemini Integration\n")

    user_input = input("Enter your prompt:\n")

    # Step 1: Call Gemini
    print("\nCalling Gemini API...\n")
    gemini_response = ask_gemini(user_input)

    print("Gemini Response:\n")
    print(gemini_response)

    # Step 2: Tokenize Response
    print("\n Tokenizing response...\n")

    tokens, token_ids = tokenize_text(gemini_response)

    # Step 3: Display Results
    print_colored_tokens(tokens)
    print_token_details(tokens, token_ids)


# Run Application
if __name__ == "__main__":
    main()