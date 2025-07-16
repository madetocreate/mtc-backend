from openai import OpenAI
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def score_task(task):
    prompt = f"Wie wichtig ist diese Aufgabe auf einer Skala von 1 bis 10? {task}"
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role":"user","content":prompt}])
    return response.choices[0].message.content.strip()
