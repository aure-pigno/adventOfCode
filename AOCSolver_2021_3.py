import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_3(AOCSolver):

    def parse(self, input):
        self.table = input.split("\n")

    def execute(self, part=1):
        if part == 1:
            gamma, epsilon = "", ""
            for i in range(0, len(self.table[0])):
                elem = self.get_bit_map(i, self.table)
                v = int(len(elem["1"]) > len(elem["0"]))
                epsilon += str(v)
                gamma += str(1 - v)
            return int(epsilon, 2) * int(gamma, 2)
        return self.get_record(self.table) * self.get_record(self.table, False)

    @staticmethod
    def get_bit_map(i, t):
        mp = {"0": [], "1": []}
        for elem in t:
            mp[elem[i]].append(elem)
        return mp

    @staticmethod
    def get_record(records, ox=True):
        for i in range(0, len(records[0])):
            hmap = AOCSolver_2021_3.get_bit_map(i, records)
            num = int(len(hmap["1"]) >= len(hmap["0"]))
            records = hmap[str(num if ox else 1 - num)]
            if len(records) == 1:
                return int(records[0], 2)
