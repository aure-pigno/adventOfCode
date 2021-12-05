def split(word):
    return [char for char in word]


def table_converter(text_table):
    return [int(i) for i in text_table]


def sum_col(table, i):
    return sum([elem[i] for elem in table])


def sum_table(table):
    return sum([sum(elem) for elem in table])


def replace(table, v, new_v):
    return [[new_v if x == v else x for x in elem] for elem in table]


def max_table(table):
    return max([max(elem) for elem in table])

def copy_table(table):
    return [elem for elem in table]


def empty_grid(x, y=None):
    return [[0 for i in range(x)] for j in range(x if y is None else y)]
