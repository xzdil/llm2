from model import llm

for i in llm.stream_complete("Привет").response_iter:
  print(i, end='')
