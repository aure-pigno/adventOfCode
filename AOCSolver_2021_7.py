import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_7(AOCSolver):

    def parse(self, input):
        self.table = helper.table_converter(input.replace("\n", "").split(","))

    def execute(self, part=1):
        p = int(helper.median(self.table)) if part == 1 else round(0.5 + (sum(self.table) - len(self.table)) / (len(self.table) - 1))
        return sum([abs(p - elem) if part == 1 else int(abs(p - elem) * (1 + abs(p - elem)) / 2) for elem in self.table])

