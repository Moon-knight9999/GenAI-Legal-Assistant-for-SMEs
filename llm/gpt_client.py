import openai

openai.api_key = "YOUR_KEY"

def explain(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content
