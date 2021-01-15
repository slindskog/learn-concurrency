import time
from urllib.request import urlopen


def get_urls_to_crawl():
    urls_list = list()
    urls_list.append('http://www.cnn.com/')
    urls_list.append('https://www.foxnews.com/')
    urls_list.append('https://www.bbc.com/')
    urls_list.append('https://www.cnbc.com')
    urls_list.append('https://www.dawn.com')
    return urls_list


if __name__ == "__main__":

    urls_to_crawl = get_urls_to_crawl()
    start = time.time()

    for url in get_urls_to_crawl():
        print(url)
        html = urlopen(url)
        text = html.read()

    elapsed = time.time() - start
    print("\n{} URLS downloaded in {:.2f}s".format(len(urls_to_crawl), elapsed))
