import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_14(AOCSolver):

    seq = ""
    v_map = {}

    def parse(self, input):
        t = input.split("\n")
        self.seq = t.pop(0)
        t.pop(0)
        for line in t:
            [p1, p2] = line.split(" -> ")
            self.v_map[p1] = p2

    def execute(self, part=1):
        pmap = {}
        it = 10 if part == 1 else 40
        for key in self.v_map:
            pmap[key] = 0
        for i in range(len(self.seq) - 1):
            pmap[self.seq[i] + self.seq[i + 1]] += 1
        for n in range(it):
            pmap = self.slide(pmap, self.v_map)
        ct = self.count(pmap, self.seq).values()
        return max(ct) - min(ct)

    @staticmethod
    def slide(count_map, v_map):
        new_map = {}
        for v in count_map:
            i1, i2 = v[0] + v_map[v], v_map[v] + v[1]
            new_map[i1] = count_map[v] if i1 not in new_map else new_map[i1] + count_map[v]
            new_map[i2] = count_map[v] if i2 not in new_map else new_map[i2] + count_map[v]
        return new_map

    @staticmethod
    def count(pmap, seq):
        new_map = {}
        for v in pmap:
            ct = pmap[v]
            [v1, v2] = helper.split(v)
            new_map[v1] = ct if v1 not in new_map else new_map[v1] + ct
            new_map[v2] = ct if v2 not in new_map else new_map[v2] + ct
        for v in new_map:
            new_map[v] = int(new_map[v]/2)
        new_map[seq[ 0]] += 1
        new_map[seq[-1]] += 1
        return new_map
