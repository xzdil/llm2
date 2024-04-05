import gradio as gr
from faiss import query_engine
from conversation import Conversation 

def gen(text, history):
  print(history)
  conversation = Conversation()
  conversation.add_user_message(text)
  prompt = conversation.get_prompt()
  chat = ''
  for token in query_engine.query(prompt).response_gen:
      chat += token
      yield chat

demo = gr.ChatInterface(fn=gen, examples=["Что такое договор о долевом участии?",
                                          "Чем отличается уполномоченная компания от застройщика?",
                                          "Как мне себя обезопасить при покупке строящегося жилья?",
                                          "Где я могу найти утвержденную форму договора долевого участия?",
                                          "Какие действия необходимо совершить дольщику для приобретения жилья в строящемся доме?",
                                          "Кто гарантирует завершение строительства жилого объекта?",
                                          "Какие меры предпринимаются для предотвращения риска двойных продаж недвижимости?",
                                          "Какие договора не безопасны?"],
                        title="ДелУчас-бот",
                        description="Это чат-бот, у которого вы можете спросить информацию о делевом участии в жилищном строительстве в РК")
demo.launch(debug=True,share=True)
