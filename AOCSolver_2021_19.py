import helper
from AOCSolver import AOCSolver
import itertools

class AOCSolver_2021_19(AOCSolver):


    d0 = [(0, 0, 0)]
    scanners = []
    def parse(self, input):
        self.scanners = [scanner(s) for s in [[eval("[" + x + "]") for x in l.split("\n")[1:]] for l in input.strip().split('\n\n')]]

    def execute(self, part=1):
        aligned = set()
        not_aligned = set()
        aligned_map = {}
        aligned.add(0)
        aligned_map[0] = self.scanners[0]
        self.scanners[0].aligned = True
        all_aligned = [tuple(x) for x in self.scanners[0].beacons]

        while len(aligned) < len(self.scanners):
            for i in range(len(self.scanners)):
                if i in aligned:
                    continue
                for j in aligned:
                    if (i, j) in not_aligned or (j, i) in not_aligned:
                        continue
                    scan_i, self.d0 = aligned_map[j].find_alignment(self.scanners[i], self.d0)
                    if scan_i is not None:
                        aligned.add(i)
                        aligned_map[i] = scan_i
                        all_aligned += [tuple(x) for x in scan_i.beacons]
                        break
                    not_aligned.add((i, j))

        if part == 1:
            return len(set(all_aligned))
        return max(max([[helper.dist_list(l1, l2) for l2 in self.d0] for l1 in self.d0]))


class scanner:

    def __init__(self, beacons):
        self.beacons = beacons

    def rotate(self, remap, negat):
        return [[negat[0] * b[remap[0]], negat[1] * b[remap[1]], negat[2] * b[remap[2]]] for b in self.beacons]

    def find_alignment(self, scan_b, d):
        in_a = set([tuple(x) for x in self.beacons])
        for remap in [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]:
            for negat in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1),
                   (-1, -1, -1)]:
                b = scan_b.rotate(remap, negat)
                for a_pos in self.beacons:
                    for b_pos in b:
                        delta = helper.sub_list(b_pos, a_pos)
                        matches = 0
                        all_remapped = []
                        for new_b in b:
                            remapped = (new_b[0] - delta[0], new_b[1] - delta[1], new_b[2] - delta[2])
                            matches += remapped in in_a
                            all_remapped.append(list(remapped))
                        if matches >= 12:
                            d.append(tuple(delta))
                            return scanner(all_remapped), d
        return None, d
