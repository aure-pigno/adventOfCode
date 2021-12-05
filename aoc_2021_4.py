import helper


def convert_table(table):
    grid_list = []
    current = []
    for elem in table:
        if elem != "":
            current.append(helper.table_converter(elem.strip().replace("  ", ",").replace(" ", ",").split(",")))
        else:
            grid_list.append(current)
            current = []
    return grid_list


def execute(numbers, grid_list, part=1):
    check = lambda g: sum([helper.sum_col(g, i) == -len(g) or sum(g[i]) == -len(g) for i in range(0, len(g))])
    for n in numbers:
        for i in range(0, len(grid_list)):
            grid = helper.replace(grid_list.pop(0), n, -1)
            if check(grid):
                if part == 1 or len(grid_list) == 0:
                    grid = helper.replace(grid, -1, 0)
                    return helper.sum_table(grid) * n
                else:
                    continue
            grid_list.append(grid)
