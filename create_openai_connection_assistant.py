import openai
import time
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Step 1: Create the Assistant
assistant = openai.beta.assistants.create(
    model="gpt-4o",  # Use "gpt-4o" for fast + high-quality generation
    name="Connections Puzzle Generator",
    instructions="""
You are a puzzle generator that creates "Connections"-style puzzles.

Generate 16 words divided into 4 distinct categories of 4 words each.
Each category should have a clear and logical connection between the words.
The words must fit only one category and not reasonably belong to another.

Make the categories vary slightly in difficulty:
- One easy category (e.g., colors, months)
- Two medium difficulty categories (e.g., Shakespeare characters, musical terms)
- One hard or tricky category (e.g., words that sound alike but are spelled differently).

Format your output only in this strict JSON structure, and nothing else:

{
  "categories": [
    {
      "name": "Category Name 1",
      "words": ["word1", "word2", "word3", "word4"]
    },
    {
      "name": "Category Name 2",
      "words": ["word1", "word2", "word3", "word4"]
    },
    {
      "name": "Category Name 3",
      "words": ["word1", "word2", "word3", "word4"]
    },
    {
      "name": "Category Name 4",
      "words": ["word1", "word2", "word3", "word4"]
    }
  ]
}

Rules:
- Do not invent fake words.
- Do not explain your answer. Only output the JSON.
- No repeated words between categories.
- Categories should cover a variety of topics (not all sports, for example).

If any rule conflicts, prioritize correctness of category groupings.
""",
    tools=[]  # No extra tools needed for now
)

print("Assistant created!")
print(f"Assistant ID: {assistant.id}")
