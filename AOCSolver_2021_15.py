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
                    neignbours = []
                    if i > 0:
                        neignbours.append(risk[j][i - 1])
                    if i < len(t[0]) - 1:
                        neignbours.append(risk[j][i + 1])
                    if j > 0:
                        neignbours.append(risk[j - 1][i])
                    if j < len(t) - 1:
                        neignbours.append(risk[j + 1][i])
                    new_risk = t[j][i]+min(neignbours)
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
        return[[ 1 if elem == 9 else elem + 1 for elem in line] for line in table]



def find_min_path(data):
    big_number = data.sum().sum()
    cost = big_number * np.ones_like(data)
    cost[- 1, - 1] = data[- 1, - 1]
    keep_going = True
    while keep_going:
        old_cost = cost
        cost = np.minimum.reduce([
            cost,
            data + shift_with_padding(cost, -1, 0, big_number),
            data + shift_with_padding(cost, 1, 0, big_number),
            data + shift_with_padding(cost, -1, 1, big_number),
            data + shift_with_padding(cost, 1, 1, big_number)
        ])
        keep_going = np.abs(cost - old_cost).any().any()
    return cost[0, 0] - data[0, 0]


def shift_with_padding(data, shift, axis, pad_value):
    shifted_data = np.roll(data, shift, axis=axis)
    null_slice = slice(None, None)
    if shift < 0:
        part_slice = slice(shift, None)
    else:
        part_slice = slice(None, shift)
    if axis == 1:
        full_slice = (null_slice, part_slice)
    else:
        full_slice = (part_slice, null_slice)
    shifted_data[full_slice] = pad_value
    return shifted_data