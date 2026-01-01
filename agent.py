import httpx
from bs4 import BeautifulSoup
from google import genai

# Your API Key
MY_API_KEY = "AIzaSyBqKxZBpIZu3HBbC8SeJ9GaLDLfY05rClg" 

client = genai.Client(api_key=MY_API_KEY)

def ask_agent(user_input):
    try:
        # Standard stable model name
        chat = client.chats.create(model="gemini-1.5-flash")
        response = chat.send_message(user_input)
        return response.text
    except Exception as e:
        # If we still get a 429, it tells the user to wait
        if "429" in str(e):
            return "⏳ The AI is taking a short break (Quota Limit). Please try again in 30 seconds!"
        return f"❌ Agent Error: {str(e)}"
# Keep your get_bni_live_text function below...

