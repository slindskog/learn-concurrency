import time
from threading import Thread, current_thread, Condition


class MultithreadedTokenBucketFilter:

    def __init__(self, MAX_TOKENS: int):
        self.MAX_TOKENS = MAX_TOKENS
        self.ONE_SECOND = 1
        self.possible_tokens = 0
        self.cond = Condition()
        dt = Thread(target=self.daemon_thread)
        dt.setDaemon(True)
        dt.start()

    def daemon_thread(self):
        while True:
            self.cond.acquire()
            if self.possible_tokens < self.MAX_TOKENS:
                self.possible_tokens = self.possible_tokens + 1
            self.cond.notify()
            self.cond.release()

            time.sleep(self.ONE_SECOND)

    def get_token(self):
        self.cond.acquire()
        while self.possible_tokens == 0:
            self.cond.wait()
        self.possible_tokens = self.possible_tokens - 1
        self.cond.release()
        print(f"Granting {current_thread().getName()} token at {time.time()}")


if __name__ == '__main__':
    token_bucket_filter = MultithreadedTokenBucketFilter(1)

    threads = [Thread(target=token_bucket_filter.get_token, name=f"Thread-{i}") for i in range(10)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
