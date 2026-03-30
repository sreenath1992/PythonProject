# Assignment 06 — Zero-Shot Chain-of-Thought

## Task
Write a script that appends a CoT trigger phrase to solve this problem **without any worked examples**:

> Vikram wants to buy a laptop costing ₹75,000. He saves ₹8,000 every month
> but spends ₹1,500 of that on subscriptions. His parents will contribute ₹15,000.
> How many months will it take him to afford the laptop?

Then run the same question **without** the trigger phrase and compare both outputs.

## Rules
- No CoT examples — only the trigger phrase activates reasoning
- Both versions (with trigger / without trigger) must be run and printed
- Label the outputs clearly: "WITHOUT CoT trigger" and "WITH CoT trigger"

## What will be checked
- Two API calls are made — one with and one without the trigger
- Both outputs are printed with clear labels
- The version with the trigger shows step-by-step working
- Final answer is correct: 9 months
