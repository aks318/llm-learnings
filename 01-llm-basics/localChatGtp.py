
import asyncio
import ollama

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

async def main():
    print("Chatbot started! Type 'exit' to quit.\n")

    while True:
        user_prompt = input("You: ").strip()

        if user_prompt.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        if not user_prompt:
            continue

        messages.append({
            "role": "user",
            "content": user_prompt
        })

        try:
            response = ollama.chat(
                model="llama3.2:1b",
                messages=messages,
                stream=True
            )
            print("Assistant: ", end="")
            assistant_message = ""

            for chunk in response:
                await asyncio.sleep(0.1)
                content = chunk["message"]["content"]
                assistant_message += " " + content
                print(content, end="", flush=True)

            messages.append({
                "role": "assistant",
                "content": assistant_message
            })
            print()

        except Exception as error:
            print(f"Error: {error}")
            messages.pop()  # Remove the failed user request

if __name__ == "__main__":
    asyncio.run(main())
