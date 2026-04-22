import openai
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY


def generate_essay_structure(history):
    prompt = f"""
    Create a 350-word essay structure.

    Include:
    - Intro (80 words)
    - Body 1 (120 words)
    - Body 2 (100 words)
    - Conclusion (50 words)

    Based on:
    {history}
    """

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content