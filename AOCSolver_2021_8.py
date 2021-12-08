import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_8(AOCSolver):

    def parse(self, input):
        self.table = input.split("\n")

    def execute(self, part=1):

        count = 0
        for line in self.table:
            elems = line.split(" | ")
            results = elems[1].split(" ")

            if part == 1:
                count += sum([len(e) == 2 or len(e) == 3 or len(e) == 4 or len(e) == 7 for e in results])
                continue

            size_map = self.compute_size_map(elems[0].split(" "))
            map = self.compute_map(size_map)

            n = self.find_numbers(map)
            count += sum([10**(3-i)*n.index("".join(sorted(helper.split(results[i])))) for i in range(0, 4)])
        return count

    @staticmethod
    def find_numbers(map):
        return [
            "".join(sorted(helper.flatten(map[0] + map[1] + map[2] + map[4] + map[5] + map[6]))),
            "".join(sorted(helper.flatten(map[2] + map[5]))),
            "".join(sorted(helper.flatten(map[0] + map[2] + map[3] + map[4] + map[6]))),
            "".join(sorted(helper.flatten(map[0] + map[2] + map[3] + map[5] + map[6]))),
            "".join(sorted(helper.flatten(map[1] + map[2] + map[3] + map[5]))),
            "".join(sorted(helper.flatten(map[0] + map[1] + map[3] + map[5] + map[6]))),
            "".join(sorted(helper.flatten(map[0] + map[1] + map[3] + map[4] + map[5] + map[6]))),
            "".join(sorted(helper.flatten(map[0] + map[2] + map[5]))),
            "".join(sorted(helper.flatten(map[0] + map[1] + map[2] + map[3] + map[4] + map[5] + map[6]))),
            "".join(sorted(helper.flatten(map[0] + map[1] + map[2] + map[3] + map[5] + map[6])))
        ]

    @staticmethod
    def compute_size_map(digits):
        size_map = {}
        for e in [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]:
            size_map[e] = []
        for w in digits:
            char = helper.split(w)
            size_map[len(char)].append(char)
        return size_map

    @staticmethod
    def compute_map(size_map):
        map = [[] for i in range(0, 7)]
        map[0] = helper.delta_list([size_map[2][0], size_map[3][0]])
        map[1] = helper.delta_list([size_map[2][0], size_map[4][0]])
        map[2] = size_map[2][0]
        map[3] = helper.delta_list([size_map[2][0], size_map[4][0]])
        map[4] = helper.delta_list([size_map[4][0], map[0], ['a', 'b', 'c', 'd', 'e', 'f', 'g']])
        map[5] = size_map[2][0]
        map[6] = helper.delta_list([size_map[4][0], map[0], ['a', 'b', 'c', 'd', 'e', 'f', 'g']])

        for e in size_map[6]:
            delta = helper.delta_list([e, size_map[7][0]])
            if delta[0] in map[2]:
                map[2] = delta
                map[5] = helper.delta_list([map[2], map[5]])
                for f in size_map[5]:
                    delta2 = helper.delta_list([e, f])
                    if len(delta2) == 1:
                        map[4] = delta2
                        map[6] = helper.delta_list([map[4], map[6]])
                        size_map[6].remove(e)
                        break

        for e in size_map[6]:
            delta = helper.delta_list([helper.flatten([map[0], map[2], map[4], map[5], map[6]]), e])
            if len(delta) == 1:
                map[1] = delta
                map[3] = helper.delta_list([map[1], map[3]])
                break
        return map