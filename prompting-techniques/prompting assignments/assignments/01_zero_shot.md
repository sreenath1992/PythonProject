# Assignment 01 — Zero-Shot Prompting

## Task

Write a Python script that sends **three different zero-shot prompts** to the Claude API using the Anthropic SDK.

Each prompt must do a different type of task:

1. Rewrite a paragraph at a 5th-grade reading level
2. Suggest 3 names for a new mobile app that helps people track their water intake
3. Write a one-line tagline for a local bakery in Hyderabad

## Rules

- No examples may be included in any prompt
- Use the `call_model()` helper from `utils.py`
- Print each prompt and response using the standard `print_result()` format

## What will be checked

- All three prompts run without errors
- None of the prompts contain examples
- Output format uses the standard PROMPT / RESPONSE separator
- Each response is relevant to its task
