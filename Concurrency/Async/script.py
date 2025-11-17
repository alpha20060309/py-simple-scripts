import asyncio
import aiohttp
import os

async def download_file(session, url, save_path):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            content = await response.read()

            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            with open(save_path, "wb") as f:
                f.write(content)

            print(f"Downloaded: {url} → {save_path}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

async def download_all(urls, dest_folder="downloads"):
    async with aiohttp.ClientSession() as session:  # <-- Fixed line: added () to create a new ClientSession instance
        tasks = []
        for i, url in enumerate(urls):
            filename = f"file_{i+1}" + os.path.splitext(url)[1]
            save_path = os.path.join(dest_folder, filename)
            tasks.append(download_file(session, url, save_path))
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = [
        "https://proliga.uz/static/club-jpeg/chelsea/logo.jpeg",
        "https://proliga.uz/static/club-jpeg/mu/logo.jpeg",
        "https://proliga.uz/static/club-jpeg/manchester-city/logo.jpeg",
    ]

    asyncio.run(download_all(urls))