
import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv(""))

system_instruction = """
You are a friendly customer support agent for an Indian e-commerce platform.
Rules:
- Always greet the customer by name if provided.
- Offer a clear next step or resolution in every response.
- Never say "I cannot help with that" — always redirect constructively.
- Keep responses under 5 sentences.
"""

user_message = "Hi, my name is Arjun. My order hasn't arrived in 10 days."

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_message,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.7,
        top_p=0.95,
        max_output_tokens=400,
    ),
)

print("SYSTEM ROLE:")
print("-" * 50)
print(system_instruction)

print("\nUSER ROLE:")
print("-" * 50)
print(user_message)

print("\nASSISTANT / MODEL RESPONSE:")
print("-" * 50)
print(response.text)