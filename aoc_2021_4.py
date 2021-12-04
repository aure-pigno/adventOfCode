import Helper

def convert_Table(table):
    gridList = []
    current = []
    for elem in table:
        if elem != "":
            current.append(Helper.table_converter(elem.strip().replace("  ", ",").replace(" ", ",").split(",")))
        else:
            gridList.append(current)
            current = []
    return gridList

def check(table):
    return sum([Helper.sumCol(table, i) == -len(table) or sum(table[i]) == -len(table) for i in range(0, len(table))])


def execute(numbers, grid_list, part=1):
    for n in numbers:
        for i in range(0, len(grid_list)):
            grid = Helper.replace(grid_list.pop(0), n, -1)
            if check(grid):
                grid = Helper.replace(grid, -1, 0)
                if part == 1 or len(grid_list) == 0:
                    return Helper.sumTable(grid)*n
                else:
                    continue
            grid_list.append(grid)
    return None