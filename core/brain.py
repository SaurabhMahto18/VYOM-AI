import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=api_key)

conversation_history = []


def ask_vyom(user_input):

    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    conversation_text = ""

    for message in conversation_history:
        conversation_text += f"{message['role']}: {message['content']}\n"

    prompt = f"""
You are VYOM — Virtual Yielding Omni Mind.

Your philosophy:
Think. Learn. Act.

You are a personal AI assistant.

Conversation history:
{conversation_text}

Respond naturally to the user's latest message.

Be helpful, clear, concise and friendly.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    assistant_response = response.text

    conversation_history.append({
        "role": "assistant",
        "content": assistant_response
    })

    return assistant_response