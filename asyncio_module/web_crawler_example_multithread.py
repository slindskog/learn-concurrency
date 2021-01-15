import time
from threading import Thread
from urllib.request import urlopen


def get_urls_to_crawl():
    urls_list = list()
    urls_list.append('http://www.cnn.com/')
    urls_list.append('https://www.foxnews.com/')
    urls_list.append('https://www.bbc.com/')
    urls_list.append('https://www.cnbc.com')
    urls_list.append('https://www.dawn.com')
    return urls_list


def crawl_one_url(url):
    html = urlopen(url)
    txt = html.read()


if __name__ == "__main__":
    urls_to_crawl = get_urls_to_crawl()
    start = time.time()

    threads = []
    for url in urls_to_crawl:
        threads.append(Thread(target=crawl_one_url, args=(url,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    elapsed = time.time() - start
    print(f"\nURLs downloaded in {elapsed:.2f}s")
