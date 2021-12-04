def split(word):
    return [char for char in word]

def table_converter(text_table):
    return [int(i) for i in text_table]

def sumTable(table, i, col = True):
    if i == -1:
        v = 0
        for elem in table:
            v += sum(elem)
        return v
    elif col:
        v = 0
        for elem in table:
            v += elem[i]
        return v
    return sum(table[i])

def replace(table, v, newV):
    newTable = []
    for elem in table:
        newTable.append([newV if x == v else x for x in elem])
    return newTable

def f_2021day3_getBitMap(i, t):
    mp = {"0": [], "1": []}
    for elem in t:
        mp[elem[i]].append(elem)
    return mp

def f_2021day3_getRecord(records, ox = True):
    for i in range(0, len(records[0])):
        hmap = f_2021day3_getBitMap(i, records)
        num = int(len(hmap["1"]) >= len(hmap["0"]))
        records = hmap[str(num if ox else 1-num)]
        if len(records) == 1:
            return int(records[0], 2)

def f_2021day4_convert_Table(table):
    gridList = []
    current = []
    while len(table) > 0:
        elem = table.pop(0)
        if elem != "":
            current.append(table_converter(elem.strip().replace("  ", ",").replace(" ", ",").split(",")))
        else:
            gridList.append(current)
            current = []
    return gridList

def f_2021day4_check(table):
    for i in range(0, len(table)):
        if sumTable(table, i) == -len(table) or sumTable(table, i, False) == -len(table):
            return True
    return False

