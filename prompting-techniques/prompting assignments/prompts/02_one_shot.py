import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import get_completion

prompt = """
Convert the following informal sentence to a professional tone.

Example:
Informal: Hey, can you tell me if you've looked at my resume yet?
Professional: I am writing to follow up on the status of my resume review.

Task:
Informal: Yo, did you check out my app yet?
Professional:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)