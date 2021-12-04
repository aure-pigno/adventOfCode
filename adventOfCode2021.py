import helper
import aoc_2021_1
import aoc_2021_2
import aoc_2021_3
import aoc_2021_4
import aoc_2021_5


def exec_2021day1():
    f = open("input/Input_2021day1.txt", "r").read()
    int_table = helper.table_converter(f.split("\n"))
    print("Day 1, Part 1:", aoc_2021_1.execute(int_table))
    print("Day 1, Part 2:", aoc_2021_1.execute(int_table, 3))


def exec_2021day2():
    f = open("input/Input_2021day2.txt", "r").read()
    text_table = f.split("\n")
    print("Day 2, Part 1:", aoc_2021_2.execute(text_table))
    print("Day 2, Part 2:", aoc_2021_2.execute(text_table, 3))


def exec_2021day3():
    f = open("input/Input_2021day3.txt", "r").read()
    text_table = f.split("\n")
    print("Day 3, Part 1:", aoc_2021_3.execute(text_table))
    print("Day 3, Part 2:", aoc_2021_3.execute(text_table, 2))


def exec_2021day4():
    f = open("input/Input_2021day4.txt", "r").read()
    text_table = f.split("\n")
    tbl = aoc_2021_4.convert_table(text_table)
    lne = (tbl.pop(0))[0]
    print("Day 4, Part 1:", aoc_2021_4.execute(lne, tbl))
    print("Day 4, Part 2:", aoc_2021_4.execute(lne, tbl, 2))


def exec_2021day5():
    f = open("input/Input_2021day5.txt", "r").read()
    text_table = f.split("\n")
    print("Day 5, Part 1:", aoc_2021_5.execute(text_table))
    print("Day 5, Part 2:", aoc_2021_5.execute(text_table, 2))
