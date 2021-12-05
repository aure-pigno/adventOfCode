import helper


def convert_table(t):
    return [helper.table_converter(elem.strip().replace(" -> ", ",").split(",")) for elem in t]

def count(table, v):
    return sum([sum([1 if x > v else 0 for x in elem]) for elem in table])

def execute(input, part=1):
    t = []
    for elem in input:
        if elem[0] == elem[2] or elem[1] == elem[3] or (part != 1 and (abs(elem[0] - elem[2]) == abs(elem[1] - elem[3]))):
            t.append(elem)
    max_x = max(helper.max_index(t, 0), helper.max_index(t, 2))
    max_y = max(helper.max_index(t, 1), helper.max_index(t, 3))

    grid = [[0 for i in range(0, max_x+1)] for j in range(0, max_y+1)]

    for elem in t:
        p1 = [elem[0], elem[1]]
        p2 = [elem[2], elem[3]]
        delta_x = 0 if p2[0] == p1[0] else 1 if p2[0] > p1[0] else -1
        delta_y = 0 if p2[1] == p1[1] else 1 if p2[1] > p1[1] else -1
        while p1 != p2:
            grid[p1[1]][p1[0]] += 1
            p1 = [p1[0] + delta_x, p1[1] + delta_y]
        grid[p2[1]][p2[0]] += 1
    return count(grid, 1)
