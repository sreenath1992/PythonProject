import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import get_completion

prompt = """
I want to save 2.5 lakhs in one year. How much should I save per month and per week? Let's think step by step.
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)