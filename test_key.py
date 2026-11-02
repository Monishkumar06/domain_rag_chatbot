import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

key = os.getenv("GROQ_API_KEY")

print("Key loaded:", bool(key))
print("Key length:", len(key) if key else 0)

try:
    client = Groq(api_key=key)

    models = client.models.list()

    print("Groq API connection: SUCCESS")

except Exception as e:
    print("Groq API connection: FAILED")
    print(type(e).__name__)
    print(str(e))