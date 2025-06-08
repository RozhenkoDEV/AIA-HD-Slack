from fastapi import APIRouter, Request
from slack_sdk import WebClient
from slack_sdk.signature import SignatureVerifier
import os
from app.rovo import handle_message

slack_router = APIRouter()
client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
verifier = SignatureVerifier(os.getenv("SLACK_SIGNING_SECRET"))

@slack_router.post("/events")
async def handle_event(req: Request):
    body = await req.body()
    if not verifier.is_valid_request(body, req.headers):
        return {"error": "invalid signature"}

    payload = await req.json()
    if "challenge" in payload:
        return {"challenge": payload["challenge"]}

    event = payload.get("event", {})
    if event.get("type") == "message":
        await handle_message(event["text"], event["user"], event["channel"])
    return {"ok": True}
