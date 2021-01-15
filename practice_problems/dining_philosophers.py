import time
import random
from threading import Thread, Semaphore


class DiningPhilosopherProblem:

    def __init__(self):
        self.forks = [Semaphore(1) for _ in range(5)]
        self.max_diners = Semaphore(4)
        self.exit = False

    def life_cycle_of_a_philosopher(self, idx):
        while self.exit is False:
            self.contemplate()
            self.eat(idx)

    def contemplate(self):
        sleep_for = random.randint(800, 1200) / 1000
        time.sleep(sleep_for)

    def eat(self, idx):
        # max_diners allows only 4 philosophers to attempt picking up forks
        self.max_diners.acquire()

        # acquire the left fork first
        self.forks[idx].acquire()

        # acquire the right fork second
        self.forks[(idx + 1) % 5].acquire()

        print(f"Philosopher {idx} is eating")

        # release forks for others to use
        self.forks[idx].release()
        self.forks[(idx + 1) % 5].release()

        self.max_diners.release()


if __name__ == '__main__':
    # Only allow 4 philosophers at any given point in time to even try to acquire forks.
    problem = DiningPhilosopherProblem()

    philosophers = [Thread(target=problem.life_cycle_of_a_philosopher, args=(idx,)) for idx in range(5)]

    for philosopher in philosophers:
        philosopher.start()

    time.sleep(6)
    problem.exit = True

    for philosopher in philosophers:
        philosopher.join()
