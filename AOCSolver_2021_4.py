import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_4(AOCSolver):
    table = []
    numbers = []

    def parse(self, input):
        self.table = []
        current = []
        for elem in input.split("\n"):
            if elem != "":
                current.append(helper.table_converter(elem.strip().replace("  ", ",").replace(" ", ",").split(",")))
            else:
                self.table.append(current)
                current = []

        self.numbers = (self.table.pop(0))[0]

    def execute(self, part=1):
        grid_list = helper.copy_table(self.table)
        check = lambda g: sum([helper.sum_col(g, i) == -len(g) or sum(g[i]) == -len(g) for i in range(0, len(g))])
        for n in self.numbers:
            for i in range(0, len(grid_list)):
                grid = helper.replace(grid_list.pop(0), n, -1)
                if check(grid):
                    if part == 1 or len(grid_list) == 0:
                        grid = helper.replace(grid, -1, 0)
                        return helper.sum_table(grid) * n
                    else:
                        continue
                grid_list.append(grid)
