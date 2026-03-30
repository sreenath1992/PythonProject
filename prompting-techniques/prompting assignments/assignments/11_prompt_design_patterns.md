# Assignment 11 — Prompt Design Patterns

## Task
Take this single product review and apply all four design patterns to it:

> "I ordered the Noise smartwatch last week. It looks premium and the step counter
> is accurate. But the sleep tracking is completely wrong — it said I slept 11 hours
> when I slept 5. Battery lasts 7 days which is great. Paid ₹3,499. Support took
> 3 days to reply and didn't resolve my issue. 3 out of 5 stars."

Apply each pattern in a separate API call:

1. **Classification** — sentiment (positive/negative/mixed), return_risk (low/medium/high)
2. **Extraction** — product, price, positives, negatives, support_experience, rating
3. **Transformation** — rewrite as a formal QA defect report for the product team
4. **Generation** — write a customer support reply email that addresses the sleep tracking bug

## Rules
- All four patterns must be separate prompts and separate API calls
- Each result must be labelled clearly before printing
- Extraction output must be one field per line (`Field: Value` format)

## What will be checked
- Four separate API calls are made
- Each pattern label is printed before its output
- Extraction output has one field per line
- Generation output reads as a real email (has greeting, body, sign-off)
