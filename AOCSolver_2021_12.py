import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_12(AOCSolver):

    map = {}

    def parse(self, input):
        for [start, end] in [line.split("-") for line in input.split("\n")]:
            self.map[start] = self.map[start] + [end] if start in self.map else [end]
            self.map[end] = self.map[end] + [start] if end in self.map else [start]

    def execute(self, part=1):
        paths = [["start"]]
        count = 0
        while len(paths) != 0:
            crt = paths.pop()
            for v in self.map[crt[-1]]:
                if v in ["start", "end"] or (helper.isLower(v) and self.max_small(crt) >= part and v in crt):
                    count += v == "end"
                    continue
                paths.append(crt + [v])
        return count

    @staticmethod
    def max_small(lst):
        return max([lst.count(e) if helper.isLower(e) else 0 for e in lst])
