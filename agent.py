import httpx
from bs4 import BeautifulSoup
from google import genai

# Use your working API Key
MY_API_KEY = "AIzaSyBqKxZBpIZu3HBbC8SeJ9GaLDLfY05rClg" 

client = genai.Client(api_key=MY_API_KEY)

def get_bni_live_text(query):
    """Lightweight web scraper that works on Python 3.14"""
    try:
        url = f"https://www.bni.com/search?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = httpx.get(url, headers=headers, follow_redirects=True, timeout=10.0)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Remove junk
        for script in soup(["script", "style"]):
            script.decompose()
        return soup.get_text()[:4000] 
    except Exception as e:
        return f"Live lookup unavailable: {str(e)}"

# In agent.py
def ask_agent(user_input):
    try:
        # Use ONLY the name 'gemini-1.5-flash'
        chat = client.chats.create(model="gemini-1.5-flash") 
        
        response = chat.send_message(user_input)
        return response.text
    except Exception as e:
        return f"❌ Agent Error: {str(e)}"

