import openai

openai.api_key = "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"

def ask_llm(chunks, question: str) -> str:
    # Prompt oluştur
    sources = []
    context = ""
    for doc in chunks:
        source = doc.metadata.get("source", "Bilinmeyen kaynak")
        context += f"(Kaynak: {source})\n{doc.page_content}\n\n"
        sources.append(source)

    prompt = f"Aşağıdaki belgeler ışığında soruyu cevapla.\n\n{context}\nSoru: {question}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content
