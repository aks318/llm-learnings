from pydantic import BaseModel

class Message(BaseModel):
    role: str
    content: str

class Conversation(BaseModel):
    messages: list[Message]


conversation = Conversation(
    messages=[
        Message(role="user", content="Hi!"),
        Message(role="assistant", content="Hello!")
    ]
)

for message in conversation.messages:
    print(message.role, message.content)