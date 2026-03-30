import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import get_completion

prompt = """
Q: A SaaS company pays ₹45,000/month for server costs.
   They also pay ₹8,000/month per developer and employ 4 developers.
   What is the total annual operating cost for servers and developers?

A: Let's work through this step by step.
   1. Monthly server cost = ₹45,000
   2. Monthly developer cost = 4 developers × ₹8,000 = ₹32,000
   3. Total monthly cost = ₹45,000 + ₹32,000 = ₹77,000
   4. Annual cost = ₹77,000 × 12 = ₹9,24,000
   Answer: The total annual operating cost is ₹9,24,000.
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)