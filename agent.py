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

def ask_agent(user_input):
    # Detect if user is asking for specific data
    if any(word in user_input.lower() for word in ["find", "chapter", "location", "near", "mumbai", "dubai"]):
        print(f"🌐 Crawling BNI.com for: {user_input}")
        live_data = get_bni_live_text(user_input)
        prompt = f"BNI SYSTEM CONTEXT:\n{live_data}\n\nUSER QUESTION: {user_input}"
    else:
        # Default BNI knowledge
        prompt = f"You are a BNI Expert. Answer this: {user_input}"

    try:
        chat = client.chats.create(
    model="gemini-1.5-flash",  # Use 1.5-flash for the most stable free quota
    config={"system_instruction": "You are the Official BNI Inquiry Counter..."}
)
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        return f"❌ Agent Error: {str(e)}"