import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_1(AOCSolver):

    def parse(self, input):
        self.table = helper.table_converter(input.split("\n"))

    def execute(self, depth=1):
        return sum([(sum(self.table[(i + 1):(i + 1) + depth]) > sum(self.table[i:i + depth]))
                    for i in range(0, len(self.table) - (depth - 1))])

    def part2(self):
        return self.execute(depth=3)
