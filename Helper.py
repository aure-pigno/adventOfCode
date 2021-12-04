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

