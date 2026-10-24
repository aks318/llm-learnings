from email import message
from typing import Literal

import asyncio

from httpx import stream
import ollama


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any
from fastapi.responses import StreamingResponse
import json

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str

class UserPromptRequest(BaseModel):
    user_prompt: str

messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful assistant. "
            "Use the entire conversation history to answer questions. "
            "Remember information the user shares within this conversation, "
            "and use it when relevant."
        )
    }
]

def stream_response(user_prompt):
    print(user_prompt)
    if user_prompt.lower() in ("exit", "quit"):
        print("Goodbye!")
        yield json.dumps({"content": "Goodbye!"}) + "\n"
        return

    messages.append({
        "role": "user",
        "content": user_prompt
    })

    try:
        response = ollama.chat(
            model= "llama3.2:1b",
            messages=messages,
            stream = True
        )

        assistant_message = ""

        for chunk in response:
            content = chunk["message"]["content"]
            assistant_message += content
            # Stream the content back to frontend
            yield json.dumps({"content": content}) + "\n"

        messages.append({
            "role": "assistant",
            "content": assistant_message
        })

    except Exception as error:
        print(f"Error: {error}")
        messages.pop()  # Remove the failed user request
        yield json.dumps({"content": "Sorry, I encountered an error processing your request."}) + "\n"

@app.post('/user_prompt')
def user_question(request: UserPromptRequest):
    return StreamingResponse(stream_response(request.user_prompt), media_type="text/event-stream")