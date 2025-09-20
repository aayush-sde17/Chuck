import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def ai_response(command):
    """Get AI response from GPT"""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"You are Chuck, a helpful voice assistant. The user said: '{command}'. Reply conversationally.",
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception:
        return "Sorry, I couldn’t connect to AI right now."
