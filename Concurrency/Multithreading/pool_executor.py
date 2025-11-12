from concurrent.futures import ThreadPoolExecutor
import time


def fetch_data(n):
    print(f"Fetching {n}")
    time.sleep(2)
    return f"Data {n}"

with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(fetch_data,[1,2,3,4,5,6]))

print(results)