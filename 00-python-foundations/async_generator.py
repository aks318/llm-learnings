import asyncio

async def generate_chunk():
    chunks = ["Hello", " from", " your", " local", " LLM!"]

    for chunk in chunks:
        await asyncio.sleep(0.5)
        yield chunk


async def main():
    async for chunk in generate_chunk():
        print(chunk, end="", flush=True)
    print()

if __name__ == "__main__":
    asyncio.run(main())