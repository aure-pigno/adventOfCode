import Helper

def f_2021day1(int_table, depth=1):
    count = 0
    for i in range(0, len(int_table) - (depth - 1)):
        count += (sum(int_table[(i + 1):(i + 1) + depth]) > sum(int_table[i:i + depth]))
    return count

def exec_2021day1():
    f = open("input/Input_2021day1.txt", "r").read()
    int_table = Helper.table_converter(f.split("\n"))
    print("Part 1:", f_2021day1(int_table))
    print("Part 2:", f_2021day1(int_table, 3))

def f_2021day2(text_table, part=1):
    x, y1, y2 = 0, 0, 0
    comp = lambda k, v: [x + v * (k == "forward"), y1 + v * y2 * (k == "forward"), y2 + v * ((k == "down") - (k == "up"))]
    for line in text_table:
        [k, v] = line.split(" ")
        [x, y1, y2] = comp(k, int(v))
    return x * y1 if part == 1 else x * y2

def exec_2021day2():
    f = open("input/Input_2021day2.txt", "r").read()
    text_table = f.split("\n")
    print("Part 1:", f_2021day2(text_table))
    print("Part 2:", f_2021day2(text_table, 3))

def f_2021day3(text_table, part=1):
    if part == 1:
        gamma, epsilon = "", ""
        for i in range(0, len(text_table[0])):
            elem = Helper.f_2021day3_getBitMap(i, text_table)
            v = int(len(elem["1"]) > len(elem["0"]))
            epsilon += str(v)
            gamma += str(1-v)
        return int(epsilon, 2)*int(gamma, 2)

    return Helper.f_2021day3_getRecord(text_table) * Helper.f_2021day3_getRecord(text_table, False)

def exec_2021day3():
    f = open("input/Input_2021day3.txt", "r").read()
    text_table = f.split("\n")
    print("Part 1:", f_2021day3(text_table))
    print("Part 2:", f_2021day3(text_table, 2))
