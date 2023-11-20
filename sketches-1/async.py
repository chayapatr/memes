import asyncio
import random
import time

async def process_single(item: str) -> str:
    """Slow I/O function to process a single element"""
    print(f"started: {item}")
    await asyncio.sleep(random.randint(1, 5))  # Simulating I/O-bound processing using asyncio.sleep
    print(f"processed: {item}")
    return f"returned {item}"

async def process_batch(batch: list[str]) -> list[str]:
    """Executes a slow I/O bound function asynchronously on a batch of samples"""
    tasks = [process_single(item) for item in batch]
    results = await asyncio.gather(*tasks)
    return results

def write_results(results: list[str]):
    print(results)

async def main():
    batches = [['a', 'b', 'c'], ['d', 'e', 'f']]

    for batch in batches:
        results = await process_batch(batch)
        write_results(results)

if __name__ == "__main__":
    asyncio.run(main())