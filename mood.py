import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def get_songs_by_mood(mood):
    
    chat = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": f"I am feeling {mood}, suggest me 5 songs with the artist name and song title,can you also explain why each song fits the mood and make sure toi give the output in a numbered format"}
        ]
    )

    return(chat.choices[0].message.content)
