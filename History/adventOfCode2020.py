import re
import Helper
def f_2020day1(int_table, n = 2):
    int_table = sorted(list(dict.fromkeys(int_table)))
    for i in range(0, len(int_table)):
        for j in range(i + 1, len(int_table)):
            if n == 2:
                if int_table[i] + int_table[j] == 2020:
                    return int_table[i] * int_table[j]
                elif int_table[i] + int_table[j] > 2020:
                    break
            else:
                for k in range(j + 1, len(int_table)):
                    if int_table[i] + int_table[j] + int_table[k] == 2020:
                        return int_table[i] * int_table[j] * int_table[k]
                    elif int_table[i] + int_table[j] + int_table[k] > 2020:
                        break

def exec_2020day1():
    f = open("input/Input_2020day1.txt", "r").read()
    int_table = Helper.table_converter(f.split("\n"))
    print("Part 1:", f_2020day1(int_table))
    print("Part 2:", f_2020day1(int_table, 3))


def f_2020day2(text_table, stage = 1):
    correct_pwd = 0
    for str in text_table:
        lne = str.split()
        range = lne[0].split("-")
        min_n = int(range[0])
        max_n = int(range[1])
        char = lne[1].replace(":", "")
        char_list = Helper.split(lne[2])
        if stage == 1:
            cnt = char_list.count(char)
            if cnt >= min_n and cnt <= max_n:
                correct_pwd = correct_pwd + 1
        else:
            if (char_list[min_n - 1] == char) != (char_list[max_n - 1] == char):
                correct_pwd = correct_pwd + 1
    return correct_pwd

def exec_2020day2():
    f = open("input/Input_2020day2.txt", "r").read()
    text_table = f.split("\n")
    print("Part 1:", f_2020day2(text_table))
    print("Part 2:", f_2020day2(text_table, 2))


def f_2020day3(text_table, x_moves, y_moves):
    int_table = [Helper.table_converter(Helper.split(elem.replace(".", "0").replace("#", "1"))) for elem in text_table]
    resp = 1
    for k in range(0, len(x_moves)):
        x, y, part_resp = 0, 0, 0
        x_len = len(int_table[0])
        y_len = len(int_table)
        while y < y_len:
            part_resp = part_resp + int_table[y][x % x_len]
            x = x + x_moves[k]
            y = y + y_moves[k]
        resp = part_resp * resp
    return resp

def exec_2020day3():
    f = open("input/Input_2020day3.txt", "r").read()
    text_table = f.split("\n")
    print("Part 1:", f_2020day3(text_table, [3], [1]))
    print("Part 2:", f_2020day3(text_table, [1, 3, 5, 7, 1], [1, 1, 1, 1, 2]))

def f_2020day4(str, stage = 1):
    text_table = str.replace("\n", " ").split("  ")
    valid_table =[]

    for elem in text_table:
        id_elements = elem.split(" ")
        hashmap = {}
        for id_elem in id_elements:
            pair = id_elem.split(":")
            hashmap[pair[0]] = pair[1]
        if len(hashmap) >= 8 or (len(hashmap) == 7 and "cid" not in hashmap):
            valid_table.append(hashmap)

    if stage == 1:
        return len(valid_table)

    valid_table2 = []
    for elem in valid_table:

        if not(elem["byr"].isnumeric() and (int(elem["byr"]) >= 1920 and int(elem["byr"]) <= 2002)): continue

        if not(elem["iyr"].isnumeric() and (int(elem["iyr"]) >= 2010 and int(elem["iyr"]) <= 2020)): continue

        if not(elem["eyr"].isnumeric() and (int(elem["eyr"]) >= 2020 and int(elem["eyr"]) <= 2030)): continue

        if re.search("#[0-9a-f]{6}", elem["hcl"]) == None: continue

        if elem["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: continue

        if len(elem["pid"]) != 9 or re.search("[0-9]{9}", elem["pid"]) == None: continue

        if re.search("[0-9]{2}in", elem["hgt"]) != None and  int(elem["hgt"].replace("in","")) >= 59 and int(elem["hgt"].replace("in","")) <= 76:
                    valid_table2.append(elem)
        elif re.search("[0-9]{3}cm", elem["hgt"]) != None and int(elem["hgt"].replace("cm","")) >= 150 and int(elem["hgt"].replace("cm","")) <= 193:
                    valid_table2.append(elem)

    return len(valid_table2)

def exec_2020day4():
    f = open("input/Input_2020day4.txt", "r").read()
    print("Part 1:", f_2020day4(f))
    print("Part 2:", f_2020day4(f, 2))

def f_2020day5(text_table, stage=1):
    seatIds = []

    for str in text_table:
        min_range_row = 0
        max_range_row = 127
        min_range_col = 0
        max_range_col = 7
        for char in str:
            if char == "F":
                max_range_row = int((max_range_row + min_range_row) / 2)
            if char == "B":
                if ((max_range_row + min_range_row) % 2) != 0:
                    min_range_row = int((1 + max_range_row + min_range_row) / 2)
                else:
                    min_range_row = int((max_range_row + min_range_row) / 2)
            if char == "L":
                max_range_col = int((max_range_col + min_range_col) / 2)
            if char == "R":
                if ((max_range_col + min_range_col) % 2) != 0:
                    min_range_col = int((1 + max_range_col + min_range_col) / 2)
                else:
                    min_range_col = int((max_range_col + min_range_col) / 2)
        seatIds.append(max_range_row * 8 + max_range_col)
    if stage == 1:
        return max(seatIds)

    fullRange = [x for x in range(1 * 8 + 7, max(seatIds) + 1)]
    for elem in seatIds:
        fullRange.remove(elem)
    return min(fullRange)

def exec_2020day5():
    f = open("input/Input_2020day5.txt", "r").read()
    text_table = f.split("\n")
    print("Part 1:", f_2020day5(text_table))
    print("Part 2:", f_2020day5(text_table, 2))

def f_2020day6_part1(str):
    text_table = str.replace("\n\n", " ").replace("\n", "").split(" ")
    text_table = [Helper.split(word) for word in text_table]
    final_table = []
    size = 0
    for elem in text_table:
        tab = list(dict.fromkeys(elem))
        final_table.append(tab)
        size += len(tab)
    return size

def f_2020day6_part2(str):
    text_table = str.split("\n\n")
    count = 0
    for elem in text_table:
        splt = elem.count("\n") + 1
        first = elem.split("\n")[0]
        elem = elem.replace("\n", "")
        for c in first:
            if elem.count(c) == splt:
                count += 1
    return count

def exec_2020day6():
    f = open("input/Input_2020day6.txt", "r").read()
    print("Part 1:", f_2020day6_part1(f))
    print("Part 2:", f_2020day6_part2(f))