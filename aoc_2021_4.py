import helper

def convert_table(table):
    gridList = []
    current = []
    for elem in table:
        if elem != "":
            current.append(helper.table_converter(elem.strip().replace("  ", ",").replace(" ", ",").split(",")))
        else:
            gridList.append(current)
            current = []
    return gridList

def check(table):
    return sum([helper.sum_col(table, i) == -len(table) or sum(table[i]) == -len(table) for i in range(0, len(table))])


def execute(numbers, grid_list, part=1):
    for n in numbers:
        for i in range(0, len(grid_list)):
            grid = helper.replace(grid_list.pop(0), n, -1)
            if check(grid):
                grid = helper.replace(grid, -1, 0)
                if part == 1 or len(grid_list) == 0:
                    return helper.sum_table(grid) * n
                else:
                    continue
            grid_list.append(grid)
    return None