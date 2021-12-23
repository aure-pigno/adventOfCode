import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_22(AOCSolver):

    def parse(self, input):
        for elem in input.replace("x","").replace("y","").replace("z","").replace("=","").split("\n"):
            v = [[int(x) for x in sub_elem.split("..")] for sub_elem in elem.split(" ")[1].split(",")]
            dict = {"is_on": "on" in elem, "x": range(v[0][0], v[0][1]+1),
                    "y": range(v[1][0], v[1][1]+1), "z": range(v[2][0], v[2][1]+1)}
            dict["len"] = len(dict["x"])*len(dict["y"])*len(dict["z"])
            self.table.append(dict)

    def execute(self, part=1):

        t = self.reduce_input(self.table) if part == 1 else helper.copy_table(self.table)
        answer = 0
        for idx, item in enumerate(t):
            if item["is_on"]:
                answer += self.count_no_overlap(item, t[idx + 1:])
        return answer

    def count_no_overlap(self, item, rest):
        overlap = []
        for item2 in rest:
            new_item = self.compute_range(item, item2)
            if new_item["len"] != 0:
                overlap.append(new_item)
        for idx, item2 in enumerate(overlap):
            item["len"] -= self.count_no_overlap(item2, overlap[idx + 1:])
        return item["len"]

    def reduce_input(self, t):
        new_t = []
        std = {"is_on": False, "x": range(-50, 51), "y": range(-50, 51), "z":range(-50, 51), "len": 1000000}
        for elem in t:
            new_item = self.compute_range(std, elem)
            if new_item["len"] != 0:
                new_t.append(new_item)
        return new_t

    @staticmethod
    def compute_range(item, item2):
        new_item = {}
        for i in item:
            if i == "is_on" or i == "len":
                new_item[i] = item2[i]
            else:
                s, e, s2, e2 = item[i][0], item[i][-1], item2[i][0], item2[i][-1]
                new_item[i] = [] if e2 < s or s2 > e else range(min(max(s2, s), e), min(max(e2, s), e) + 1)
        new_item["len"] = len(new_item["x"])*len(new_item["y"])*len(new_item["z"])
        return new_item
