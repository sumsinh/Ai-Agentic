from rag import ask_question

question = input("Ask a question: ")

result = ask_question(question)

print("\nAnswer:\n")
print(result["answer"])

print("\nRetrieved Chunks:\n")

for i, chunk in enumerate(result["context"],1):
    print(f"\nChunk {i}\n")
    print(chunk)

print("\nConfidence Score:", result["score"])