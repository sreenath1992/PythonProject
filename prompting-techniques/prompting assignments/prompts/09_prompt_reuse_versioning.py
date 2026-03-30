
import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import get_completion

prompt_v1 = "Summarize this text"

prompt_v2 = """
Summarize this text in 3 bullet points with simple language.
"""

text = "AI helps automate tasks and improves efficiency across industries."

response1 = get_completion(prompt_v1 + "\n" + text)
response2 = get_completion(prompt_v2 + "\n" + text)

print("PROMPT V1:")
print("-" * 50)
print(prompt_v1)

print("\nRESPONSE V1:")
print("-" * 50)
print(response1)

print("\nPROMPT V2:")
print("-" * 50)
print(prompt_v2)

print("\nRESPONSE V2:")
print("-" * 50)
print(response2)