import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_25(AOCSolver):

    def parse(self, input):
        self.table = [helper.split(line) for line in input.split("\n")]

    def execute(self, part=1):
        steps = 0
        while True:
            steps += 1
            if self.move(True) + self.move(False) == 0:
                break
        return steps

    def move(self, east=True):
        char = ">" if east else "v"
        count, movable = 0, []
        compute_indexes = lambda i, j: [i, (j + 1) % len(self.table[0])] if east else [(i + 1) % len(self.table), j]
        for i in range(len(self.table)):
            for j in range(len(self.table[0])):
                indexes = compute_indexes(i, j)
                if self.table[i][j] == char and self.table[indexes[0]][indexes[1]] == ".":
                    movable.append((i, j))
                    count += 1
        for i, j in movable:
            indexes = compute_indexes(i, j)
            self.table[i][j] = "."
            self.table[indexes[0]][indexes[1]] = char
        return count
