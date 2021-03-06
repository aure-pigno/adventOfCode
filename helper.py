def split(word):
    return [char for char in word]


def table_converter(text_table):
    return [int(i) for i in text_table]


def split_convert(word):
    return [int(v) for v in split(word)]


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


def copy_map(v_map):
    new_map = {}
    for key in v_map:
        new_map[key] = v_map[key]
    return new_map


def get_cols(table):
    return list(map(list, zip(*table)))


def empty_grid(x, y=None):
    return [[0 for i in range(x)] for j in range(x if y is None else y)]


def multiply_list(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


def median(lst):
    l, s = len(lst), sorted(lst)
    return (sum(s[l//2-1:l//2+1])/2.0, s[l//2])[l % 2] if l else None


def average(lst):
    return sum(lst)/len(lst)


def flatten(t):
    return [item for sublist in t for item in sublist]


def delta_list(lsts):
    lst = flatten(lsts)
    return [v for v in lst if lst.count(v) == 1]


def add(table, v):
    return [[x + v for x in line] for line in table]


def sum_list(l1, l2):
    return [l1[i] + l2[i] for i in range(len(l1))]


def sub_list(l1, l2):
    return [l1[i] - l2[i] for i in range(len(l1))]


def dist_list(l1, l2):
    return sum([abs(l1[i] - l2[i]) for i in range(len(l1))])


def remove_elems(l, s):
    for v in l:
        s = s.replace(v,"")
    return s


def contains(table, v):
    return sum([sum([x == v for x in line]) for line in table]) != 0


def get_neighbours(t, j, i, diag=False):
    ngh = []
    if i > 0:
        ngh.append(t[j][i - 1])
        if diag:
            if j > 0:
                ngh.append([j - 1][i - 1])
            if j < len(t) - 1:
                ngh.append([j + 1][i - 1])
    if i < len(t[0]) - 1:
        ngh.append(t[j][i + 1])
        if diag:
            if j > 0:
                ngh.append([j - 1][i + 1])
            if j < len(t) - 1:
                ngh.append([j + 1][i + 1])
    if j > 0:
        ngh.append(t[j - 1][i])
    if j < len(t[0]) - 1:
        ngh.append(t[j + 1][i])
    return ngh


def string_to_hex(str):
    v_map = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
    return "".join([v_map[v] for v in split(str)])
