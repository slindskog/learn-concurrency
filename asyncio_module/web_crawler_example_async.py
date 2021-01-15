import time
import aiohttp
import asyncio


async def crawl_one_url(url, session):
    get_request = session.get(url)
    result = await get_request
    txt = await result.text()
    get_request.close()
    return txt


async def crawl_urls(urls_to_crawl):
    session = aiohttp.ClientSession()
    work_to_do = []
    for url in urls_to_crawl:
        work_to_do.append(crawl_one_url(url, session))
    result = await asyncio.gather(*work_to_do)
    await session.close()
    return result


def main():
    t0 = time.time()
    urls_to_crawl = get_urls_to_crawl()
    asyncio.run(crawl_urls(urls_to_crawl))
    elapsed = time.time() - t0
    print(f"\nURLs downloaded in {elapsed:.2f}s")


def get_urls_to_crawl():
    urls_list = list()
    urls_list.append('http://www.cnn.com/')
    urls_list.append('https://www.foxnews.com/')
    urls_list.append('https://www.bbc.com/')
    urls_list.append('https://www.cnbc.com')
    urls_list.append('https://www.dawn.com')
    return urls_list


if __name__ == "__main__":
    main()
