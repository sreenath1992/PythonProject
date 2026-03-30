# Assignment 04 — Multi-Shot Prompting

## Task
Create a multi-shot classifier that labels **customer complaint messages** with both a category and an urgency level.

Categories: `billing | technical | shipping | account | general`
Urgency: `low | medium | high`

Write at least 7 examples covering different combinations, then test on:
- "My account was hacked and someone changed my email."
- "I haven't received my order from 3 weeks ago."
- "Can you tell me your business hours?"

## Rules
- Minimum 7 examples required
- Each example must show both category AND urgency
- Output format per example: `Category: X | Urgency: Y`

## What will be checked
- At least 7 examples are present
- Both fields (category and urgency) are present in every output
- The 3 test messages are all classified
- Examples are stored in a reusable list, not inline strings
