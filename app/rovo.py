import os
import httpx
from slack_sdk import WebClient

async def handle_message(text, user, channel):
    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://api.rovo.ai/chat",
            headers={"Authorization": f"Bearer {os.getenv('ROVO_API_KEY')}"},
            json={"prompt": text}
        )
        answer = res.json().get("response", "🤖 Я пока не знаю, как ответить.")

    WebClient(token=os.getenv("SLACK_BOT_TOKEN")).chat_postMessage(
        channel=channel,
        text=answer
    )
