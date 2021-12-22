import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_15(AOCSolver):

    def parse(self, input):
        self.table = [[int(x) for x in helper.split(line)] for line in input.split("\n")]

    def execute(self, part=1):
        t = helper.copy_table(self.table)
        if part == 2:
            t = self.compute_table(t)
        risk = [[10000 for x in line] for line in t]
        risk[0][0] = 0
        bool = True
        while bool:
            bool = False
            for j in range(len(t)):
                for i in range(len(t[0])):
                    new_risk = t[j][i]+min(helper.get_neighbours(risk, j, i) )
                    prisk = risk[j][i]
                    risk[j][i] = min(prisk, new_risk)
                    bool = bool or risk[j][i] != prisk
        return risk[-1][-1] - risk[0][0]

    def compute_table(self, table):
        new_c = helper.copy_table(table)
        for i in range(4):
            table = self.add1(table)
            for j in range(len(table)):
                new_c[j] = new_c[j] + table[j]
        table = helper.copy_table(new_c)
        for i in range(4):
            table = self.add1(table)
            new_c = new_c + table
        return new_c

    @staticmethod
    def add1(table):
        return[[1 if elem == 9 else elem + 1 for elem in line] for line in table]
