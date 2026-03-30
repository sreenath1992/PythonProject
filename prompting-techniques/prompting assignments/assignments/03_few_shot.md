# Assignment 03 — Few-Shot Prompting

## Task
Build a few-shot prompt that classifies **job posting titles** into one of four departments:
- engineering
- marketing
- design
- operations

Write at least 3 examples covering different departments, then test on these titles:
- "Senior React Developer"
- "Growth Hacking Intern"
- "UX Researcher"
- "Logistics Coordinator"

## Rules
- Minimum 3, maximum 5 examples in the prompt
- Store examples as a list of tuples, not hardcoded strings
- Build the prompt programmatically using a loop

## What will be checked
- Examples are stored as a list and built with a loop
- All 4 test titles are classified
- Labels match one of the four valid department names
- Script runs cleanly with no errors
