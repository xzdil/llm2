from model import llm

for i in llm.stream_complete("Привет"):
  print(i, end='')
