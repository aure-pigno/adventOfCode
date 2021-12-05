import helper


def convert_table(t):
    return [helper.table_converter(elem.strip().replace(" -> ", ",").split(",")) for elem in t]


def execute(input, part=1):
    t = [e for e in input if e[0] == e[2] or e[1] == e[3] or (part != 1 and (abs(e[0] - e[2]) == abs(e[1] - e[3])))]
    grid = helper.empty_grid(helper.max_t(t) + 1)
    for elem in t:
        [p1, p2] = [[elem[0], elem[1]], [elem[2], elem[3]]]
        delta_x = 0 if p2[0] == p1[0] else 1 if p2[0] > p1[0] else -1
        delta_y = 0 if p2[1] == p1[1] else 1 if p2[1] > p1[1] else -1
        while p1 != p2:
            grid[p1[1]][p1[0]] += 1
            p1 = [p1[0] + delta_x, p1[1] + delta_y]
        grid[p1[1]][p1[0]] += 1
    return sum([sum([1 if x > 1 else 0 for x in e]) for e in grid])
