import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "models/gemini-2.5-flash-lite"  # Free-tier supported

def format_answer(question, raw_answer):
    try:
        prompt = f"""
You are an academic chatbot for ACE Engineering College.

Question:
{question}

Raw Information:
{raw_answer}

Rules:
- Rewrite clearly
- Use bullet points if applicable
- Do NOT add new information
- Keep professional and concise
"""

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        return response.text.strip()

    except Exception as e:
        print("Gemini fallback used:", e)
        return raw_answer
