import openai
import db

openai.api_key = "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"

my_prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: 오늘 뭐해?\nAI: 누워서티비 보는중\nHuman: 오늘 뭐해?\nAI: 저는 집이 편해요.\nHuman:"
def get_text(text):
  global my_prompt
  my_prompt = my_prompt + "\nHuman: " + text + "\nAI: "
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=my_prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )
  ai = response.choices[0].text
  my_prompt = my_prompt + ai
  return ai

while True:
  message = input('나 : ')
  if message == '배우기':
    q = input('Q : ')
    a = input('A : ')
    my_prompt = my_prompt + "\nHuman: " + q + "\nAI: " + a
    print('AI : 알겠어요')
  else: print(f'AI: {get_text(message)}')