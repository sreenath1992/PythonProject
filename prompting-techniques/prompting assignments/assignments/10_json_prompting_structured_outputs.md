# Assignment 10 — JSON Prompting & Structured Outputs

## Task
Write a script that extracts structured data from this news snippet and parses it into Python:

> "Zepto, the Mumbai-based quick commerce startup founded in 2021 by Aadit Palicha
> and Kaivalya Vohra, raised $200 million in a Series E round in 2023. The company
> currently employs around 1,000 full-time staff and operates across 10 Indian cities."

Your JSON schema must include:
- `company` (string)
- `city` (string)
- `founded_year` (integer)
- `founders` (list of strings)
- `funding_usd_million` (number)
- `funding_round` (string)
- `employee_count` (integer)
- `cities_count` (integer)

## Rules
- Prompt must say "Return ONLY valid JSON — no prose, no markdown"
- Use `json.loads()` to parse the response
- Wrap parsing in `try/except json.JSONDecodeError`
- After parsing, print at least 3 individual fields by key name

## What will be checked
- JSON schema matches all 8 required fields
- `json.loads()` is used with error handling
- At least 3 fields are printed individually after parsing
- Script runs without errors
