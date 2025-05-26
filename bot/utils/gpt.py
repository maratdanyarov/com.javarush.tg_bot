import os
import logging
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def ask_gpt(prompt: str) -> str:
    try:
        logger.info(f"Asking GPT {prompt}")
        response = await client.chat.completions.create(
                model="gpt-4.1",
                messages=[{"role": "user", "content": prompt}]
            )
        logger.info(f"Received response: {response.choices[0].message.content.strip()}")
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"GPT error: {e}")
        return f"Error accessing ChatGPT: {e}"

