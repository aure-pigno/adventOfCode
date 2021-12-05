from abc import abstractmethod
from datetime import datetime


class AOCSolver:

    def __init__(self, n):
        t1 = datetime.now()
        f = open("input/Input_2021day"+str(n)+".txt", "r").read()
        self.parse(f)
        t2 = datetime.now()
        print("Day", n, "init:", (t2 - t1))

    def part1(self):
        return self.execute(1)

    def part2(self):
        return self.execute(2)

    def solve(self, n=1):
        t1 = datetime.now()
        if n == 1:
            result = self.part1()
        else:
            result = self.part2()
        t2 = datetime.now()
        print("Part", n, "result:", result, "duration:", (t2 - t1))

    @abstractmethod
    def parse(self, input):
        pass

    @abstractmethod
    def execute(self, part):
        pass
