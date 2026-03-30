# Assignment 09 — Prompt Reuse & Versioning

## Task
You are building a prompt that writes a **short product description** for an e-commerce listing.

Create two versions of this prompt and run both on the same product:

**Product:** Bamboo water bottle, 750ml, keeps drinks cold for 24 hours, price ₹899

- **v1.0.0** — just the task, no structure
- **v2.0.0** — add role, target audience, output format (Title + 3 bullets + CTA), and at least 2 constraints

After both run, print a version comparison summary showing what changed between v1 and v2.

## Rules
- Version strings must be stored as constants (`PROMPT_V1_VERSION`, `PROMPT_V2_VERSION`)
- Both prompts must use the same product input (no hardcoding different products)
- The comparison summary must be printed as plain text after both responses

## What will be checked
- Both version constants are defined
- The same product text is used for both versions
- v2 output has a clear Title + bullets + CTA structure
- Comparison summary is printed at the end
