import asyncio
import multiprocessing
import requests
import threading
import time


urls_1 = ["https://www.monkeyuser.com",
          "https://www.airbnb.com",
          "https://www.commitstrip.com",
          "https://www.example.com",
          "https://www.google.com"]

urls_2 = ["https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com",
          "https://www.airbnb.com"]

urls_3 = ["https://www.airbnb.com",
          "https://www.airbnb.com"]


class AsyncScrapper:
    def __init__(self, urls):
        self.urls = urls

    async def curl(self, counter):
        response = requests.get(self.urls[counter])
        print(self.urls[counter])
        print(response.text)
        counter += 1

    async def main(self):
        curls = (self.curl(i) for i in range(len(self.urls)))
        await asyncio.gather(*curls)


class SyncScrapper:
    def __init__(self, urls):
        self.urls = urls

    def curl(self, counter):
        response = requests.get(self.urls[counter])
        print(self.urls[counter])
        print(response.text)

    def main(self):
        for i in range(len(self.urls)):
            self.curl(i)


class ThreadScrapper:
    def __init__(self, urls):
        self.urls = urls

    def curl(self, counter):
        response = requests.get(self.urls[counter])
        print(self.urls[counter])
        print(response.text)

    def main(self):
        threads = []
        for i in range(len(self.urls)):
            thread = threading.Thread(target=self.curl(i))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


class ParallelScrapper:
    def __init__(self, urls):
        self.urls = urls

    def curl(self, counter):
        response = requests.get(self.urls[counter])
        print(self.urls[counter])
        print(response.text)

    def main(self):
        processes = []
        for i in range(len(self.urls)):
            process = multiprocessing.Process(target=self.curl, args=(i,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()


if __name__ == '__main__':
    urls = urls_2

    # async_start_time = time.perf_counter()
    # async_scrapper = AsyncScrapper(urls)
    # asyncio.run(async_scrapper.main())
    # async_elapsed = time.perf_counter() - async_start_time
    # print(f"async_elapsed: {async_elapsed}")
    # "async_elapsed: 16.251925965999998"
    # "python concurrent.py  1.26s user 0.19s system 8% cpu 16.615 total"

    # sync_start_time = time.perf_counter()
    # sync_scrapper = SyncScrapper(urls)
    # sync_scrapper.main()
    # sync_elapsed = time.perf_counter() - sync_start_time
    # print(f"sync_elapsed: {sync_elapsed}")
    # "sync_elapsed: 28.349678090999998"
    # "python concurrent.py  1.21s user 0.18s system 4% cpu 28.716 total"

    # thread_start_time = time.perf_counter()
    # thread_scrapper = ThreadScrapper(urls)
    # thread_scrapper.main()
    # thread_elapsed = time.perf_counter() - thread_start_time
    # print(f"thread_elapsed: {thread_elapsed}")
    # "thread_elapsed: 16.017910892"
    # "python concurrent.py  1.22s user 0.19s system 8% cpu 16.385 total"

    parallel_start_time = time.perf_counter()
    parallel_scrapper = ParallelScrapper(urls)
    parallel_scrapper.main()
    parallel_elapsed = time.perf_counter() - parallel_start_time
    print(f"parallel_elapsed: {parallel_elapsed}")
    # "parallel_elapsed: 5.474943297"
    # "python concurrent.py  11.43s user 2.05s system 231% cpu 5.825 total"
