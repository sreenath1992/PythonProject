"""
Prompting Techniques
Example: Prompt Structuring Basics
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import get_completion

prompt = """
Role: Career Coach

Task: Suggest career options

Context: Student interested in AI and coding

Constraints: Keep it simple, max 3 options

Output Format:
- Option 1
- Option 2
- Option 3
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)