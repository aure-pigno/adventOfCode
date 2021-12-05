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

def max_index(table, i):
    return max([elem[i] for elem in table])
