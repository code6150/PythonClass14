import os
import openai

openai.api_key = "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"

my_prompt = "You: What have you been up to?\nFriend: Watching old movies.\nYou: What's the name of the movie?\nFriend:"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=my_prompt,
  temperature=0.5,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=["You:"]
)

print(response.choices[0].text)