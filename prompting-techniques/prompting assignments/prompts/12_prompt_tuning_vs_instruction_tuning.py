
import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import get_completion

simple_prompt = """
Explain the difference between the following three concepts clearly 
and concisely for a developer who is new to LLMs:

1. Prompt Engineering
2. Prompt Tuning
3. Instruction Tuning

For each one, cover:
- What it is (one sentence definition)
- Who does it (developer / ML engineer / AI lab)
- What changes (text / soft tokens / model weights)
- When you would use it
- One concrete example

Format each section with a clear heading.
"""

response = get_completion(simple_prompt)

print("PROMPT:")
print("-" * 50)
print(simple_prompt)

print("\nMODEL EXPLANATION:")
print("-" * 50)
print(response)

print("\n" + "=" * 70)
print("IMPORTANT NOTE")
print("-" * 50)
print("Prompt engineering = writing better prompts as a user.")
print("Prompt tuning = training-time method where a learned prompt is optimized.")
print("Instruction tuning = training the model on many instruction-response examples.")
print("So in normal API usage, we are doing prompt engineering, not prompt tuning.")