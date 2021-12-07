import helper
from datetime import datetime
from AOCSolver import AOCSolver


class AOCSolver_2021_6(AOCSolver):

    def parse(self, input):
        self.table = helper.table_converter(input.replace("\n", "").split(","))

    def execute(self, it=1, repro=6, mx=8):
        lst = [0 for i in range(mx + 1)]
        for elem in self.table:
            lst[elem] += 1
        for l in range(0, it):
            self.slide(lst, repro, mx)
        return sum(lst)

    @staticmethod
    def slide(lst, repro, mx):
        temp = lst[0]
        for i in range(0, mx):
            lst[i] = lst[i + 1]
        lst[mx] = temp
        lst[repro] = lst[repro] + lst[mx]

    def part1(self):
        return self.execute(it=80)

    def part2(self):
        return self.execute(it=256)
