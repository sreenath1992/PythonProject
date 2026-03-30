import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import get_completion

prompt = """
Label the email intent and urgency level.

Email: My item arrived broken, I want my money back immediately.
Intent: Refund Request | Urgency: High

Email: How do I change my password?
Intent: Account Support | Urgency: Medium

Email: Thanks for the great service!
Intent: Feedback | Urgency: Low

Email: I was charged twice for my subscription and I'm very upset.
Intent: Billing Issue | Urgency: High

Email: I'd like to return this shirt because it doesn't fit.
Intent:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)