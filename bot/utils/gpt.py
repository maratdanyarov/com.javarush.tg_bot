import os
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def ask_gpt(prompt: str) -> str:
    try:
        response = await client.chat.completions.create(
                model="gpt-4.1",
                messages=[{"role": "user", "content": prompt}]
            )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error accessing ChatGPT: {e}"

