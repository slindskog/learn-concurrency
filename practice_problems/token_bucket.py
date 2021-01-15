import time
from threading import Thread, Lock, current_thread


class TokenBucketFilter:

    def __init__(self, MAX_TOKENS):
        self.MAX_TOKENS = MAX_TOKENS
        self.last_request_time = time.time()
        self.possible_tokens = 0
        self.lock = Lock()

    def get_token(self):
        with self.lock:
            self.possible_tokens += int((time.time() - self.last_request_time))
            self.possible_tokens = max(self.possible_tokens, self.MAX_TOKENS)
            if self.possible_tokens == 0:
                time.sleep(1)
            else:
                self.possible_tokens -= 1
            self.last_request_time = time.time()
            print(f"Granting {current_thread().getName()} token at {time.time()}")


if __name__ == '__main__':
    token_bucket_filter = TokenBucketFilter(1)

    time.sleep(5)

    threads = [Thread(target=token_bucket_filter.get_token) for _ in range(10)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
