import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_13(AOCSolver):

    folds = []

    def parse(self, input):
        max_x, max_y = 0, 0
        tbl = input.split("\n")
        found = False
        for i in range(len(tbl)):
            line = tbl[-(i+1)]
            if line == "":
                found = True
                self.folds = [k for k in reversed(self.folds)]
                self.table = [[0 for x in range(max_x * 2 + 1)] for y in range(max_y * 2 + 1)]
            elif found:
                [x, y] = [int(v) for v in line.split(",")]
                self.table[y][x] = 1
            elif not(found):
                is_x, v = int("x" in line), int(line.split("=")[1])
                max_x, max_y = max(max_x, v * is_x), max(max_y, v * (1 - is_x))
                self.folds.append([is_x * v, (1-is_x) * v])

    def execute(self, part=1):
        tbl = helper.copy_table(self.table)
        for elem in self.folds:
            tbl = self.fold(tbl, max(elem), elem[0] == 0)
            if part == 1:
                return helper.sum_table(tbl)
        for elem in tbl:
            print("".join(["#" if e != 0 else " " for e in elem]))

    @ staticmethod
    def fold(table, pos, h):
        sx = len(table[0]) if h else int(len(table[0]) / 2)
        sy = int(len(table) / 2) if h else len(table)
        new_table = [[0 for x in range(sx)] for y in range(sy)]
        for y in range(len(table)):
            for x in range(len(table[0])):
                if (h and y < pos) or (not(h) and x < pos):
                    new_table[y][x] = max(table[y][x], new_table[y][x])
                elif h and y > pos:
                    new_table[2 * pos - y][x] = max(table[y][x], new_table[2 * pos - y][x])
                elif not(h) and x > pos:
                    new_table[y][2 * pos - x] = max(table[y][x], new_table[y][2 * pos - x])
        return new_table
