from faiss import query_engine
for token in query_engine.query("Какие договора не безопасны").response_gen:
    print(token, end="")
