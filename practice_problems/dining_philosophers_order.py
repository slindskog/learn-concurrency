import time
import random
from threading import Thread, Semaphore


class DiningPhilosopherProblem:

    def __init__(self):
        self.forks = [Semaphore(1) for _ in range(5)]
        self.exit = False

    def life_cycle_of_a_philosopher(self, idx):
        while self.exit is False:
            self.contemplate()
            self.eat(idx)

    def contemplate(self):
        sleep_for = random.randint(800, 1200) / 1000
        time.sleep(sleep_for)

    def acquire_forks_for_right_handed_philosopher(self, idx):
        self.forks[idx].acquire()
        self.forks[(idx + 1) % 5].acquire()

    def acquire_forks_for_left_handed_philosopher(self, idx):
        self.forks[(idx + 1) % 5].acquire()
        self.forks[idx].acquire()

    def eat(self, idx):
        # We randomly selected the philospher with idx 3 as left-handed.
        # All others must be right-handed to avoid deadlock.
        if idx == 3:
            self.acquire_forks_for_left_handed_philosopher(idx)
        else:
            self.acquire_forks_for_right_handed_philosopher(idx)

        print(f"Philosopher {idx} is eating")

        # release forks for others to use
        self.forks[idx].release()
        self.forks[(idx + 1) % 5].release()


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
