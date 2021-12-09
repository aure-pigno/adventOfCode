import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_9(AOCSolver):

    known_indexes = []
    def parse(self, input):
        self.table = [helper.table_converter(helper.split(line)) for line in input.split("\n")]

    def execute(self, part=1):
        v = []
        for j in range(len(self.table)):
            for i in range(len(self.table[0])):
                if j != 0 and self.table[j][i] >= self.table[j-1][i]:
                    continue
                if j != len(self.table)-1 and self.table[j][i] >= self.table[j+1][i]:
                    continue
                if i != 0 and self.table[j][i] >= self.table[j][i-1]:
                    continue
                if i != len(self.table[0])-1 and self.table[j][i] >= self.table[j][i+1]:
                    continue
                self.known_indexes = []
                v.append(self.table[j][i] + 1 if part == 1 else self.propagate(j, i))
        return sum(v) if part == 1 else helper.multiply_list(sorted(v)[(len(v)-3):len(v)])


    def propagate(self, j,i):
        if self.known_indexes.__contains__([j, i]) or i < 0 or i == len(self.table[0]) or j < 0 or j == len(self.table) or self.table[j][i] == 9:
            return 0
        else:
            self.known_indexes.append([j, i])
            return 1 + self.propagate(j - 1, i) + self.propagate(j + 1, i) + self.propagate(j, i - 1) + self.propagate(j, i + 1)
