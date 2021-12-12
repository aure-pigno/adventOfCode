import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_11(AOCSolver):

    known_indexes = []
    def parse(self, input):
        self.table = [helper.table_converter(helper.split(line)) for line in input.split("\n")]

    def execute(self, part=1):
        n = 100 if part == 1 else 100000
        tbl = helper.copy_table(self.table)
        count = 0
        for loop in range(n):
            self.known_indexes = []
            tbl = helper.add(tbl, 1)
            c = True
            while c:
                c = False
                for j in range(len(tbl)):
                    for i in range(len(tbl[0])):
                        if tbl[j][i] < 10 or [j, i] in self.known_indexes:
                            continue
                        self.known_indexes.append([j, i])
                        for [y, x] in helper.flatten([[[j + dy, i + dx] for dx in range(-1,2)] for dy in range(-1,2)]):
                            if x != -1 and y != -1 and x != len(tbl[0]) and y != len(tbl):
                                tbl[y][x] += 1
                                if tbl[y][x] == 10 and [y, x] not in self.known_indexes:
                                    c = True
            if part != 1 and len(self.known_indexes) == 100:
                return loop + 1

            tbl = self.replace(tbl)
            count += len(self.known_indexes)
        return count

    @staticmethod
    def replace(tbl):
        return [[0 if v >= 10 else v for v in line] for line in tbl]