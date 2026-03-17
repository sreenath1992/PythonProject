
from google import genai
from config import GOOGLE_API_KEY, GEMINI_MODEL


# Initialize Gemini
def initialize_gemini():
    if not GOOGLE_API_KEY:
        raise ValueError("Missing GEMINI_API_KEY. Set it in your environment before running the app.")

    return genai.Client(api_key=GOOGLE_API_KEY)


# Ask Gemini
def ask_gemini(prompt: str) -> str:
    try:
        client = initialize_gemini()
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )
        return response.text or "No text was returned by the Gemini API."
    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"
