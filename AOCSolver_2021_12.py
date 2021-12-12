import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_12(AOCSolver):

    map = {}

    def parse(self, input):
        for [p1, p2] in [line.split("-") for line in input.split("\n")]:
            self.map[p1] = self.map[p1] + [p2] if p1 in self.map else [p2]
            self.map[p2] = self.map[p2] + [p1] if p2 in self.map else [p1]

    def execute(self, part=1):
        paths = [["start"]]
        count = 0
        while len(paths) != 0:
            crt = paths.pop()
            for v in self.map[crt[-1]]:
                if v in ["start", "end"] or (v.islower() and self.max_low(crt) >= part and v in crt):
                    count += v == "end"
                    continue
                paths.append(crt + [v])
        return count

    @staticmethod
    def max_low(lst):
        return max([lst.count(e) if e.islower() else 0 for e in lst])
