import time
from urllib.request import urlopen
from multiprocessing import Process


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

    processes = []
    for url in urls_to_crawl:
        processes.append(Process(target=crawl_one_url, args=(url,)))

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    elapsed = time.time() - start
    print(f"\nURLs downloaded in {elapsed:.2f}s")
