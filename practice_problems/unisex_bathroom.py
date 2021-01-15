import time
from threading import Thread, Condition, Semaphore


class UnisexBathroomProblem:

    def __init__(self):
        self.in_use_by = None
        self.emps_in_bathroom = 0
        self.max_emps_sem = Semaphore(3)
        self.cond = Condition()

    def use_bathroom(self, name):
        # Simulate using a bathroom
        print(f"\n{name}, is using the bathroom. {self.emps_in_bathroom} employees are in the bathroom")
        time.sleep(3)
        print(f"\n{name} is done using the bathroom")

    def male_use_bathroom(self, name):
        with self.cond:
            while self.in_use_by == "female":
                self.cond.wait()
            self.max_emps_sem.acquire()
            self.emps_in_bathroom += 1
            self.in_use_by = "male"

        self.use_bathroom(name)
        self.max_emps_sem.release()

        with self.cond:
            self.emps_in_bathroom -= 1
            if self.emps_in_bathroom == 0:
                self.in_use_by = None

            self.cond.notifyAll()

    def female_use_bathroom(self, name):
        with self.cond:
            while self.in_use_by == "male":
                self.cond.wait()

            self.max_emps_sem.acquire()
            self.emps_in_bathroom += 1
            self.in_use_by = "female"

        self.use_bathroom(name)
        self.max_emps_sem.release()

        with self.cond:
            self.emps_in_bathroom -= 1
            if self.emps_in_bathroom == 0:
                self.in_use_by = None
            self.cond.notifyAll()


if __name__ == '__main__':
    problem = UnisexBathroomProblem()

    female1 = Thread(target=problem.female_use_bathroom, args=("Lisa",))
    male1 = Thread(target=problem.male_use_bathroom, args=("John",))
    male2 = Thread(target=problem.male_use_bathroom, args=("Bob",))
    female2 = Thread(target=problem.female_use_bathroom, args=("Natasha",))
    male3 = Thread(target=problem.male_use_bathroom, args=("Anil",))
    male4 = Thread(target=problem.male_use_bathroom, args=("Wentao",))
    male5 = Thread(target=problem.male_use_bathroom, args=("Nikhil",))
    male6 = Thread(target=problem.male_use_bathroom, args=("Paul",))
    male7 = Thread(target=problem.male_use_bathroom, args=("Klemond",))
    male8 = Thread(target=problem.male_use_bathroom, args=("Bill",))
    male9 = Thread(target=problem.male_use_bathroom, args=("Zak",))

    female1.start()
    male1.start()
    male2.start()
    time.sleep(1)
    female2.start()
    male3.start()
    male4.start()
    male5.start()
    male6.start()
    male7.start()
    male8.start()
    male9.start()

    female1.join()
    female2.join()
    male1.join()
    male2.join()
    male3.join()
    male4.join()
    male5.join()
    male6.join()
    male7.join()
    male8.join()
    male9.join()

    print("Employees in bathroom at the end {0}".format(problem.emps_in_bathroom))
