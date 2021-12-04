import Helper

def convert_Table(table):
    gridList = []
    current = []
    while len(table) > 0:
        elem = table.pop(0)
        if elem != "":
            current.append(Helper.table_converter(elem.strip().replace("  ", ",").replace(" ", ",").split(",")))
        else:
            gridList.append(current)
            current = []
    return gridList

def check(table):
    for i in range(0, len(table)):
        if Helper.sumTable(table, i) == -len(table) or Helper.sumTable(table, i, False) == -len(table):
            return True
    return False

def execute(numbers, grid_list, part=1):
    for n in numbers:
        for i in range(0, len(grid_list)):
            grid = Helper.replace(grid_list.pop(0), n, -1)
            if check(grid):
                grid = Helper.replace(grid, -1, 0)
                sum = Helper.sumTable(grid, -1)
                if part == 1 or len(grid_list) == 0:
                    return sum*n
                else:
                    continue
            grid_list.append(grid)
    return None