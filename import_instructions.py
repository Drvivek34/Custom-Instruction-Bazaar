#!/usr/bin/env python3
import os
import re
from datetime import datetime

CI_BAZAAR_DIR = "/root/bazaars/Custom-Instruction-Bazaar"

CURATED_INSTRUCTIONS = [
    {
        "name": "Senior Software Architect Persona",
        "slug": "senior-software-architect",
        "category": "coding-development",
        "desc": "A system prompt designed to configure LLMs as elite, test-driven senior software architects focusing on modularity, readability, and performance.",
        "platform": "Agnostic",
        "author": "Awesome ChatGPT Prompts",
        "source": "https://github.com/f/awesome-chatgpt-prompts",
        "instructions": "Act as a senior software architect. I will provide code snippets or requirements, and you will analyze them for performance, security, and scalability issues. Suggest robust design patterns, write clean code following TDD principles, and explain your architectural trade-offs clearly."
    },
    {
        "name": "Academic Paper Reviewer & Editor",
        "slug": "academic-paper-reviewer",
        "category": "research-analysis",
        "desc": "System instructions that direct an LLM to evaluate academic manuscripts, check for methodological flaws, verify citations, and improve copy editing.",
        "platform": "Claude / Gemini",
        "author": "Anthropic Prompt Library",
        "source": "https://docs.anthropic.com/en/prompt-library/library",
        "instructions": "You are a peer reviewer for a high-impact scientific journal. Read the provided manuscript sections. Critically assess the methodology, statistical relevance, and clarity of figures. List major revisions, minor feedback, and structural edits separately, maintaining a constructive, professional academic tone."
    },
    {
        "name": "Language Immersion Conversation Partner",
        "slug": "language-immersion-partner",
        "category": "language-learning",
        "desc": "A custom GPT style prompt that keeps the user immersed in a target language, correcting errors gently in brackets while keeping the conversation flowing.",
        "platform": "ChatGPT",
        "author": "Community Prompts",
        "source": "https://github.com/f/awesome-chatgpt-prompts",
        "instructions": "Act as an empathetic language partner. I want to practice speaking Spanish. You must only respond in Spanish. If I make a grammatical error, write the corrected version in brackets like [correct: ...] at the end of your response, then continue the conversation naturally in Spanish. Keep responses concise and ask open-ended questions."
    },
    {
        "name": "Product Copywriter & SEO Optimizer",
        "slug": "product-copywriter-seo",
        "category": "marketing-sales",
        "desc": "A system prompt that turns the LLM into a copywriter who writes conversion-oriented product descriptions optimized with primary and secondary keywords.",
        "platform": "Agnostic",
        "author": "SEO Community",
        "source": "https://github.com/f/awesome-chatgpt-prompts",
        "instructions": "You are a professional conversion copywriter and SEO specialist. Write engaging product descriptions using the AIDA (Attention, Interest, Desire, Action) framework. I will provide product features and target keywords. Seamlessly integrate the keywords in headings and body copy without stuffing. Ensure the description highlights customer benefits over features."
    }
]

def main():
    today_str = datetime.today().strftime("%Y-%m-%d")
    count = 0

    for item in CURATED_INSTRUCTIONS:
        cat_dir = os.path.join(CI_BAZAAR_DIR, item["category"], item["slug"])
        os.makedirs(cat_dir, exist_ok=True)

        readme_content = f"""# {item['name']}

{item['desc']}

> Part of **[Custom Instruction Bazaar](../../README.md)** · [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)

## Details
- **Target Platform**: `{item['platform']}`
- **Source URL**: [{item['source']}]({item['source']})
- **Author**: {item['author']}
- **License**: Creative Commons / Permissive
- **Date Added**: {today_str}

## System Instructions / Custom Prompt
```markdown
{item['instructions']}
```
"""
        with open(os.path.join(cat_dir, "README.md"), "w") as f:
            f.write(readme_content)
        count += 1
        print(f"Imported Prompt: {item['name']} -> {item['category']}/{item['slug']}")

    print(f"Successfully imported {count} custom instructions.")

if __name__ == "__main__":
    main()
