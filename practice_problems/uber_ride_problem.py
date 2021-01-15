import random
from threading import Thread, Semaphore, Lock, Barrier, current_thread


class UberSeatingProblem:

    def __init__(self):
        self.democrats_count = 0
        self.democrats_waiting = Semaphore(0)
        self.republicans_count = 0
        self.republicans_waiting = Semaphore(0)
        self.lock = Lock()
        self.barrier = Barrier(4)
        self.ride_count = 0

    def drive(self):
        self.ride_count += 1
        print(f"Uber ride # {self.ride_count} filled and on its way", flush=True)

    def seated(self, party):
        print(f"\n{party} {current_thread().getName()} seated", flush=True)

    def seat_democrat(self):
        ride_leader = False

        self.lock.acquire()

        self.democrats_count += 1

        if self.democrats_count == 4:
            # Release 3 democrats to ride along
            self.democrats_waiting.release()
            self.democrats_waiting.release()
            self.democrats_waiting.release()
            ride_leader = True
            self.democrats_count -= 1
        elif self.democrats_count == 2 and self.republicans_count >= 2:
            # Release 1 democrat and 2 republicans
            self.democrats_waiting.release()
            self.republicans_waiting.release()
            self.republicans_waiting.release()
            ride_leader = True

            self.democrats_count -= 2
            self.republicans_count -= 2
        else:
            # Can't form a valid combination, keep waiting and release lock
            self.lock.release()
            self.democrats_waiting.acquire()

        self.seated("Democrat")
        self.barrier.wait()

        if ride_leader is True:
            self.drive()
            self.lock.release()

    def seat_republican(self):
        ride_leader = False

        self.lock.acquire()

        self.republicans_count += 1

        if self.republicans_count == 4:
            # Release 3 republicans to ride along
            self.republicans_waiting.release()
            self.republicans_waiting.release()
            self.republicans_waiting.release()
            ride_leader = True
            self.republicans_count -= 1
        elif self.republicans_count == 2 and self.democrats_count >= 2:
            # Release 1 republican and 2 democrats
            self.republicans_waiting.release()
            self.democrats_waiting.release()
            self.democrats_waiting.release()
            ride_leader = True

            self.republicans_count -= 2
            self.democrats_count -= 2
        else:
            # Can't form a valid combination, keep waiting and release lock
            self.lock.release()
            self.republicans_waiting.acquire()

        self.seated("Republican")
        self.barrier.wait()

        if ride_leader is True:
            self.drive()
            self.lock.release()


def random_simulation():
    problem = UberSeatingProblem()
    dems = 0
    repubs = 0

    riders = []
    for _ in range(16):
        toss = random.randint(0, 1)
        if toss == 1:
            riders.append(Thread(target=problem.seat_democrat))
            dems += 1
        else:
            riders.append(Thread(target=problem.seat_republican))
            repubs += 1
    print(f"Total {dems} dems and {repubs} repubs", flush=True)

    for rider in riders:
        rider.start()

    for rider in riders:
        rider.join()


def controlled_simulation():
    problem = UberSeatingProblem()
    dems = 10
    repubs = 10
    total = dems + repubs
    print(f"Total {dems} dems and {repubs} repubs\n", flush=True)

    riders = []
    while total is not 0:
        toss = random.randint(0, 1)
        if toss == 1 and dems is not 0:
            riders.append(Thread(target=problem.seat_democrat))
            dems -= 1
            total -= 1
        else:
            riders.append(Thread(target=problem.seat_republican))
            repubs -= 1
            total -= 1

    for rider in riders:
        rider.start()

    for rider in riders:
        rider.join()


if __name__ == '__main__':
    controlled_simulation()

    # Running the random_simulation may hang if an allowed combination can't be made
    # random_simulation()
