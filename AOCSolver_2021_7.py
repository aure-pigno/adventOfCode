import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_7(AOCSolver):

    def parse(self, input):
        self.table = helper.table_converter(input.replace("\n", "").split(","))

    def execute(self, part=1):
        p1 = int(helper.median(self.table)) if part == 1 else int(helper.average(self.table))
        pr1, pr2, p2 = 0, 0, p1 + 1
        for elem in self.table:
            pr1 += abs(p1 - elem) if part == 1 else int(abs(p1 - elem) * (1 + abs(p1 - elem)) / 2)
            pr2 += abs(p2 - elem) if part == 1 else int(abs(p2 - elem) * (1 + abs(p2 - elem)) / 2)
        return min(pr1, pr2)
