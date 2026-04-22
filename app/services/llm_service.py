import openai
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY


def generate_question(user_input, history):
    prompt = f"""
    You are an essay coach.

    Conversation:
    {history}

    User said:
    {user_input}

    Ask a deep reflective question to extract life story.
    """

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content