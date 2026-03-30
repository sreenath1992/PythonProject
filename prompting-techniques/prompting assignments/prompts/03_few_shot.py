import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import get_completion

prompt = """
Classify the sentiment and category of the following customer feedback.

Feedback: The food was delicious and arrived early!
Sentiment: Positive | Category: Food Quality

Feedback: My order was cold and the driver was rude.
Sentiment: Negative | Category: Service

Feedback: I never received my package and nobody is helping.
Sentiment:
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)