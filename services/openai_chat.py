from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(question: str, contexts: list[str]) -> str:
    context_text = "\n\n".join(contexts)
    prompt = f"""
You are a legal assistant. Answer the following question using the context below.
If relevant, include references in parentheses like (source:page).

Context:
{context_text}

Question: {question}
"""
    response = client.chat.completions.create(
        model="gpt-4.1-nano-2025-04-14",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=500
    )
    return response.choices[0].message.content
