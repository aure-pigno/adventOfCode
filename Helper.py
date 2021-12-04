def split(word):
    return [char for char in word]

def table_converter(text_table):
    return [int(i) for i in text_table]

def sumCol(table, i):
    return sum([elem[i] for elem in table ])

def sumTable(table):
    return sum([sum(elem) for elem in table])

def replace(table, v, newV):
    return [[newV if x == v else x for x in elem] for elem in table]