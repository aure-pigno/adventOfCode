import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_8(AOCSolver):

    sequence = []

    def parse(self, input):
        self.table = [[elem.split(" ") for elem in line.split(" | ")]for line in input.split("\n")]

    def execute(self, part=1):
        if part == 1:
            return sum([sum([len(e) != 5 and len(e) != 6 for e in line[1]]) for line in self.table])
        return sum([sum([10**(3-i)*self.compute_sequence(l[0], i).index(sorted(helper.split(l[1][i]))) for i in range(0, 4)]) for l in self.table])

    # . 0 .
    # 1 . 2
    # . 3 .
    # 4 . 5
    # . 6 .
    def compute_sequence(self, digits, i=0):
        if i == 0:
            size_map = self.compute_size_map(digits)
            map = [[] for i in range(0, 7)]
            map[0] = helper.delta_list([size_map[2][0], size_map[3][0]]) # diff(1, 7)

            for n in size_map[6]: # search 6
                delta = helper.delta_list([n, size_map[7][0]]) # diff between 8 and (0, 6 or 9)
                if delta[0] in size_map[2][0]: # if delta is in map 2 (n is 6)
                    map[2] = delta
                    map[5] = helper.delta_list([size_map[2][0], delta])
                    six = n
                    size_map[6].remove(n)
                    break

            for n in size_map[5]: # search 5
                delta = helper.delta_list([six, n]) # diff between 6 and (2, 3 or 5)
                if len(delta) == 1: # only one change with 6 (n is 5)
                    map[4] = delta
                    map[6] = helper.delta_list([size_map[3][0], size_map[4][0], ['a', 'b', 'c', 'd', 'e', 'f', 'g'] , delta])
                    break

            for n in size_map[6]: # search 0
                delta = helper.delta_list([helper.flatten(map), n])
                if len(delta) == 1:
                    map[1] = delta
                    map[3] = helper.delta_list([size_map[2][0], size_map[4][0], delta])
                    break
            self.find_numbers(map)
        return self.sequence

    @staticmethod
    def compute_size_map(digits):
        size_map = {2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
        for w in digits:
            size_map[len(w)].append(helper.split(w))
        return size_map

    def find_numbers(self, map):
        self.sequence = [
            sorted(helper.flatten(map[0] + map[1] + map[2] + map[4] + map[5] + map[6])),
            sorted(helper.flatten(map[2] + map[5])),
            sorted(helper.flatten(map[0] + map[2] + map[3] + map[4] + map[6])),
            sorted(helper.flatten(map[0] + map[2] + map[3] + map[5] + map[6])),
            sorted(helper.flatten(map[1] + map[2] + map[3] + map[5])),
            sorted(helper.flatten(map[0] + map[1] + map[3] + map[5] + map[6])),
            sorted(helper.flatten(map[0] + map[1] + map[3] + map[4] + map[5] + map[6])),
            sorted(helper.flatten(map[0] + map[2] + map[5])),
            sorted(helper.flatten(map[0] + map[1] + map[2] + map[3] + map[4] + map[5] + map[6])),
            sorted(helper.flatten(map[0] + map[1] + map[2] + map[3] + map[5] + map[6]))
        ]