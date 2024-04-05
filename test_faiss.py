from faiss import query_engine
for token in query_engine.query(prompt).response_gen:
    print(token, end="")
