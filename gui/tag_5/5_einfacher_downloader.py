"""
Download von URLs (Quellcode).
Tool zum Einlesen

"""

import requests
from pathlib import Path
import threading
import random
from concurrent.futures import ThreadPoolExecutor


BASE_PATH = Path(__file__).parent
DATA_DIR = BASE_PATH / "data"

proxy = {
    "http": "http://proxywbs:3128",
    "https": "http://proxywbs:3128"
}

URLS = [
    "https://www.google.com/",
    "https://www.facebook.com/",
    "https://www.amazon.com/",
    "https://www.youtube.com/",
    "https://www.wikipedia.org/",
    "https://www.twitter.com/",
    "https://www.instagram.com/",
    "https://www.netflix.com/",
    "https://www.linkedin.com/",
    "https://www.reddit.com/",
    "https://www.apple.com/",
    "https://www.microsoft.com/",
    "https://www.yahoo.com/",
    "https://www.twitch.tv/",
    "https://www.github.com/",
    "https://www.stackoverflow.com/",
    "https://www.quora.com/",
    "https://www.medium.com/",
    "https://www.nytimes.com/",
    "https://www.wikipedia.org/"
]


def save_data_as_file(data: str, filename: str) -> None:
    with open(DATA_DIR / filename, mode="w", encoding="utf-8") as f:
        f.write(data)


def download_page(url):
    """download an url with requests library."""
    response = requests.get(url, proxies=proxy)
    filename = str(random.random()) + ".html"
    save_data_as_file(response.text, filename=filename)
    print("saved ...")


def modern_threaded_downloader():
    """Threaded Download of urls. Moderne Variante"""
    with ThreadPoolExecutor(max_workers=8) as executor:
        for url in URLS:
            print(f"Modern Threaded Downloading {url} ...")
            executor.submit(download_page, url=url)


def threaded_downloader() -> None:
    threads = []
    for url in URLS:
        print(f"Threaded Downloading {url} ...")
        t = threading.Thread(target=download_page, args=(url,))  # Thread erstellen
        t.start()
        threads.append(t)
    [t.join() for t in threads] # hier auf die Beendigung der Threads warten



def classic_downloader() -> None:
    for url in URLS:
        print(f"Downloading {url} ...")
        download_page(url)


if __name__ == "__main__":
    # download_page(URLS[0])
    # classic_downloader()
    # threaded_downloader()
    modern_threaded_downloader()







# url = URLS[0]
# response_standort = requests.get("https://www.wikipedia.org/" , proxies=proxy)
# response_standort = requests.get(url, proxies=proxy)
# response_de = requests.get(url)
# data = response_standort.text
# print(data)