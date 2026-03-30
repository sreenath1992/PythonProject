
import sys
from pathlib import Path
import json

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import get_completion

text = """
Rahul Mehta joined Infosys in 2019 as a software engineer based in Pune.
He was promoted to senior engineer in 2022 and currently earns 18 LPA.
He holds a B.Tech in Computer Science from VIT University.
"""
 
prompt = """
Extract information from the text below.
 
Return only valid JSON.
Do not include markdown.
Do not include code fences.
 
Use this exact structure:
{
  "name": "string",
  "company": "string",
  "location": "string",
  "current_role": "string",
  "years_at_company": 0,
  "salary_lpa": 0
}
 
Rules:
- Use only information explicitly stated in the text
- years_at_company should be calculated from 2019 to 2022
- salary_lpa should be a number, not a string
 
Text:
""" + text.strip()

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nRaw Response:")
print("-" * 50)
print(response)

print("\nParsed JSON:")
print("-" * 50)

try:
    data = json.loads(response)
    print(json.dumps(data, indent=2))
except json.JSONDecodeError:
    print("The response was not valid JSON.")