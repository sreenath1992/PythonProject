
import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import get_completion

review_text = """
ustomer review — Posted on 14 March 2025
Product: CloudDesk Pro Wireless Keyboard

I've been using this keyboard for three months now. The build quality is solid 
and typing feels great, but the Bluetooth connection drops every hour or so which 
is really frustrating during video calls. Battery life is excellent — I charge it 
once a month. I contacted support twice and they were helpful but the issue 
isn't fixed yet. Paid ₹4,500 for it. Would not buy again at this price.
"""

# Pattern 1: Classification
classification_prompt = f"""
Classify the review below across three dimensions.
Reply with exactly three lines, no extra text:
Sentiment: positive | negative | mixed
Recommend: yes | no | conditional  
Priority (for support team): low | medium | high | critical

Review:
{review_text}
"""

# Pattern 2: Extraction
extraction_prompt = f"""
Extract the following fields from the review.
Return each field on its own line as "Field: Value".
If a field is not mentioned, write "Field: not mentioned".

Fields to extract:
- Product name
- Price paid (in ₹)
- Usage duration
- Positive aspects (comma-separated)
- Negative aspects (comma-separated)
- Support contacted (yes/no)
- Would buy again (yes/no)


Review:
{review_text}
"""

# Pattern 3: Transformation
transformation_prompt = f"""
Transform the customer review below into a concise internal bug report
for the product engineering team. Use this format:

Title: (one line, problem-focused)
Reported by: Customer (anonymous)
Product: 
Severity: Low | Medium | High | Critical
Issue summary: (2–3 sentences, technical focus)
Steps to reproduce: (if inferable from review)
Customer impact: (business risk, one sentence)

Review:
{review_text}
"""

# Pattern 4: Generation
generation_prompt = f"""
Using the customer review below as context, write a professional 
customer support reply email from the company.

Rules:
- Acknowledge the specific issue (Bluetooth drops) and apologise.
- Mention that the engineering team is aware of this.
- Offer a concrete next step: firmware update link or refund option.
- End with a goodwill gesture (discount code for next purchase).
- Tone: warm, accountable, solution-focused. Under 120 words.

Review:
{review_text}
"""

classification_response = get_completion(classification_prompt)
extraction_response = get_completion(extraction_prompt)
transformation_response = get_completion(transformation_prompt)
generation_response = get_completion(generation_prompt)

print("PATTERN 1 — CLASSIFICATION")
print("-" * 50)
print(classification_response)

print("\nPATTERN 2 — EXTRACTION")
print("-" * 50)
print(extraction_response)

print("\nPATTERN 3 — TRANSFORMATION")
print("-" * 50)
print(transformation_response)

print("\nPATTERN 4 — GENERATION")
print("-" * 50)
print(generation_response)