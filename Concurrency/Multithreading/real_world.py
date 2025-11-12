import requests
from concurrent.futures import ThreadPoolExecutor

from urllib3 import response

urls = [
    "https://proliga.uz",
    "https://httpbin.org/get",
    "https://api.github.com"
]

def download(url):
    response = requests.get(url)
    print(f"{url} -> {response.status_code}")

with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(download, urls)