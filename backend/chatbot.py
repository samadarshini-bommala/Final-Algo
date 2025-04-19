import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_answer(chat_history):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_history,
            temperature=0.7,
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"
