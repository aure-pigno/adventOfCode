import helper


def convert_table(t):
    return [helper.table_converter(elem.strip().replace(" -> ", ",").split(",")) for elem in t]


def execute(input, part=1):
    t = [e for e in input if e[0] == e[2] or e[1] == e[3] or (part != 1 and (abs(e[0] - e[2]) == abs(e[1] - e[3])))]
    grid = helper.empty_grid(helper.max_table(t) + 1)
    for elem in t:
        [p1, p2] = [[elem[0], elem[1]], [elem[2], elem[3]]]
        dx = 0 if p2[0] == p1[0] else 1 if p2[0] > p1[0] else -1
        dy = 0 if p2[1] == p1[1] else 1 if p2[1] > p1[1] else -1
        while p1 != p2:
            grid[p1[1]][p1[0]] += 1
            p1 = [p1[0] + dx, p1[1] + dy]
        grid[p1[1]][p1[0]] += 1
    return sum([sum([1 if x > 1 else 0 for x in e]) for e in grid])