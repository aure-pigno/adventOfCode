import helper
from AOCSolver import AOCSolver

class AOCSolver_2021_1(AOCSolver):
    int_table = []

    def parse(self, input):
        self.int_table = helper.table_converter(input.split("\n"))

    def execute(self, depth=1):
        return sum([(sum(self.int_table[(i + 1):(i + 1) + depth]) > sum(self.int_table[i:i + depth])) for i in
                    range(0, len(self.int_table) - (depth - 1))])

    def part1(self):
        return self.execute()

    def part2(self):
        return self.execute(depth=3)
