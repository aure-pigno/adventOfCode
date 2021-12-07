import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_7(AOCSolver):

    def parse(self, input):
        self.table = helper.table_converter(input.replace("\n", "").split(","))

    def execute(self, part=1):
        count = 0
        for p in range(min(self.table), max(self.table)+1):
            fuel = 0
            for elem in self.table:
                delta = abs(p - elem)
                fuel += delta if part == 1 else delta * (delta + 1)/2
            count = fuel if count == 0 else min(fuel, count)
        return count
