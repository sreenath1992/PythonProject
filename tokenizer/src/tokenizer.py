
from transformers import AutoTokenizer
from colorama import Fore, Style, init
from config import TOKENIZER_MODEL

# Initialize colorama
init(autoreset=True)

# Load Tokenizer
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_MODEL)

# Color Palette
COLORS = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.LIGHTRED_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTYELLOW_EX,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX,
]


# Tokenize Text
def tokenize_text(text: str):
    tokens = tokenizer.tokenize(text)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)

    return tokens, token_ids


# Print Colored Tokens
def print_colored_tokens(tokens):
    print("\n Colored Tokens:\n")

    for i, token in enumerate(tokens):
        color = COLORS[i % len(COLORS)]
        print(color + token, end=" ")

    print("\n")


# Print Token Details
def print_token_details(tokens, token_ids):
    print("\n Token Details:\n")

    for token, token_id in zip(tokens, token_ids):
        print(f"{token:15} -> {token_id}")

    print("\nTotal Tokens:", len(tokens))