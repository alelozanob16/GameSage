from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key= os.getenv("OPENROUTER_API_KEY")
)

completion = client.chat.completions.create(
  model="deepseek/deepseek-prover-v2:free",
  messages=[
    {
      "role": "user",
      "content": "Tell objectively about the best storytelling vido games of all time."
    }
  ]
)
print(completion.choices[0].message.content)