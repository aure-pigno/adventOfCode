import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_7(AOCSolver):

    def parse(self, input):
        self.table = helper.table_converter(input.replace("\n", "").split(","))

    def execute(self, part=1):
        p = round(helper.median(self.table)) if part == 1 else int(helper.average(self.table))
        return sum([int(abs(p - elem)) if part == 1 else int(abs(p - elem)) * int(1 + abs(p - elem))/2 for elem in self.table])
