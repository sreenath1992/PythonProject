# Assignment 07 — System, User, and Assistant Roles

## Task
Build a **two-turn conversation** with Claude acting as a strict fitness coach.

System prompt rules:
- Always address the user by name (use "Arjun")
- Never recommend skipping rest days
- Keep every response under 4 sentences
- If asked about diet, always recommend consulting a nutritionist

Turn 1 (user): "I want to build muscle in 3 months. Where do I start?"
Turn 2 (user): "Should I work out every single day to get faster results?"

## Rules
- System prompt must include all four rules above
- Both turns must be sent in a single API call (full history in messages list)
- Print the full conversation: system rules → user turn 1 → response 1 → user turn 2 → response 2

## What will be checked
- System prompt is present and contains all four rules
- Both user turns are in the messages list
- The model addresses the user as "Arjun"
- Response to turn 2 respects the "never skip rest days" rule
