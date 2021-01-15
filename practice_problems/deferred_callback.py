import time
import math
import heapq
from threading import Thread, Condition


class DeferredCallBackExecutor:

    def __init__(self):
        self.actions = []
        self.cond = Condition()
        self.sleep = 0

    def add_action(self, action):
        # Add exec_at time for the action
        action.execute_at = time.time() + action.exec_secs_after
        self.cond.acquire()
        heapq.heappush(self.actions, action)
        self.cond.notify()
        self.cond.release()

    def start(self):
        while True:
            self.cond.acquire()

            while len(self.actions) is 0:
                self.cond.wait()

            while len(self.actions) is not 0:
                # Calculate sleep duration
                next_action = self.actions[0]
                sleep_for = next_action.execute_at - math.floor(time.time())
                if sleep_for <= 0:
                    # Time to execute action
                    break
                self.cond.wait(timeout=sleep_for)

            action_to_execute_now = heapq.heappop(self.actions)
            action_to_execute_now.action(*(action_to_execute_now,))
            self.cond.release()


# Class representing an action
class DeferredAction:

    def __init__(self, exec_secs_after, name, action):
        self.exec_secs_after = exec_secs_after
        self.name = name
        self.action = action
        self.execute_at = None

    def __lt__(self, other):
        return self.execute_at < other.execute_at


def say_hi(action):
    print(f"Hi, I am {action.name} executed at {time.time()} and required at {time.time()}")


if __name__ == '__main__':
    action1 = DeferredAction(3, ("A",), say_hi)
    action2 = DeferredAction(2, ("B",), say_hi)
    action3 = DeferredAction(1, ("C",), say_hi)
    action4 = DeferredAction(7, ("D",), say_hi)

    executor = DeferredCallBackExecutor()
    t = Thread(target=executor.start, daemon=True)
    t.start()

    executor.add_action(action1)
    executor.add_action(action2)
    executor.add_action(action3)
    executor.add_action(action4)

    # Wait for all actions to execute
    time.sleep(15)
