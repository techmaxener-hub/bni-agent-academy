import httpx
from bs4 import BeautifulSoup
from google import genai

# Your API Key
MY_API_KEY = "AIzaSyBqKxZBpIZu3HBbC8SeJ9GaLDLfY05rClg" 

client = genai.Client(api_key=MY_API_KEY)

def ask_agent(user_input):
    # List of possible model addresses to prevent 404
    models_to_try = ["gemini-1.5-flash", "gemini-2.0-flash-exp"]
    
    last_error = ""
    for model_name in models_to_try:
        try:
            # We use a simple chat creation
            chat = client.chats.create(model=model_name)
            response = chat.send_message(user_input)
            return response.text
        except Exception as e:
            last_error = str(e)
            continue # Try the next name if this one 404s
            
    return f"❌ Agent Error (Tried all models): {last_error}"

# Keep your get_bni_live_text function below...
