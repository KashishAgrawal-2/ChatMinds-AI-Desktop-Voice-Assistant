import os
import openai
from config import apikey

openai.api_key = apikey


def ai(prompt):
  openai.api_key = apikey
  text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  # todo: Wrap this inside of a  try catch block
  # print(response["choices"][0]["text"])
  text += response["choices"][0]["text"]
  if not os.path.exists("Openai"):
    os.mkdir("Openai")

  # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
  with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
    f.write(text)