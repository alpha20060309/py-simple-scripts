import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data")
    await asyncio.sleep(sleep_time)
    return {"id": id, "Sample data": f"Sample data from coroutine {id}"}

async def main():
    results = await asyncio.gather(fetch_data(1,2), fetch_data(2,1), fetch_data(3,3))

    for result in results:
        print(f"Received result {result}")


asyncio.run(main())