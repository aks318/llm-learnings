from pydantic import BaseModel
import httpx
import asyncio

async def fetchData(url: str):
    retryable_status_codes = {429, 500, 502, 503, 504}
    max_attempts = 3
    retry_delays = [1, 2]

    async with httpx.AsyncClient() as client:
        for attempt in range(max_attempts):
            try:
                response = await client.get(url)
                response.raise_for_status()
                return response.json()
            except httpx.ReadError as Error:
                print(f"Network error: {Error}")

            except httpx.HTTPStatusError as error:
                status_code = error.response.status_code

                if status_code not in retryable_status_codes:
                    raise
                print(f"HTTP {status_code}: request failed")

            if attempt < max_attempts -1:
                delay = retry_delays[attempt]
                print(f"Retry in {delay} s")
                await asyncio.sleep(delay)

        raise RuntimeError(
            f"Request failed after {max_attempts} attempts: {url}"
        )


async def main():
    url = "https://jsonplaceholder.typicode.com/todos/"
    try:
        data = await fetchData(url)
        print("Request successful!")
        print(data)
    except (RuntimeError, httpx.HTTPStatusError) as error:
        print(f"Request failed: {error}")

asyncio.run(main())
