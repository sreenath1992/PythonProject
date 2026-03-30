# Assignment 08 — Prompt Structuring Basics

## Task
Write a structured prompt using XML sections to generate a **LinkedIn job post** for the following role:

- Company: BrightMind EdTech, Bengaluru
- Role: Full Stack Developer (React + Node.js)
- Experience: 2–4 years
- Salary: ₹12–18 LPA
- Perks: Remote-friendly, health insurance, learning budget

Your prompt must include all of these sections:
`<role>`, `<task>`, `<context>`, `<constraints>`, `<output_format>`

## Rules
- All five XML sections must be present
- Constraints must include: max 200 words, no buzzwords like "rockstar" or "ninja", end with a clear CTA
- Output format must specify: Post title, Body, Hashtags (5 max)

## What will be checked
- All five XML sections are present in the prompt
- The generated post is under 200 words
- No buzzwords appear in the output
- Hashtags are included and 5 or fewer
