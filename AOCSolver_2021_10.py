import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_10(AOCSolver):

    def execute(self, part=1):
        map = {"(":")","{":"}","<":">", "[":"]", "":""}
        incorrect = {")": 0, "}": 0, ">": 0, "]": 0}
        incorrect_ratio1 = {")": 3, "}": 1197, ">": 25137, "]": 57}
        incorrect_ratio2 = {"(": 1, "{": 3, "<": 4, "[": 2}
        v_list = []
        for l in self.table:
            last_open = []
            inc = False
            for c in helper.split(l):
                if c in map:
                    last_open.append(c)
                elif c in incorrect:
                    v = last_open[-1]
                    last_open.pop()
                    if map[v] != c:
                        incorrect[c] += incorrect_ratio1[c]
                        inc = True
                        break
            if inc:
                continue
            count = 0
            while len(last_open) != 0:
                v = last_open[-1]
                last_open.pop()
                count = count * 5 + incorrect_ratio2[v]
            v_list.append(count)

        if part == 1:
            return sum([incorrect[i] for i in incorrect])
        return sorted(v_list)[int(len(v_list)/2)]
