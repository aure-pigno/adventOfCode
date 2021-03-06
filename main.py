from AOCSolver_2021_1 import AOCSolver_2021_1
from AOCSolver_2021_2 import AOCSolver_2021_2
from AOCSolver_2021_3 import AOCSolver_2021_3
from AOCSolver_2021_4 import AOCSolver_2021_4
from AOCSolver_2021_5 import AOCSolver_2021_5
from AOCSolver_2021_6 import AOCSolver_2021_6
from AOCSolver_2021_7 import AOCSolver_2021_7
from AOCSolver_2021_8 import AOCSolver_2021_8
from AOCSolver_2021_9 import AOCSolver_2021_9
from AOCSolver_2021_10 import AOCSolver_2021_10
from AOCSolver_2021_11 import AOCSolver_2021_11
from AOCSolver_2021_12 import AOCSolver_2021_12
from AOCSolver_2021_13 import AOCSolver_2021_13
from AOCSolver_2021_14 import AOCSolver_2021_14
from AOCSolver_2021_15 import AOCSolver_2021_15
from AOCSolver_2021_16 import AOCSolver_2021_16
from AOCSolver_2021_17 import AOCSolver_2021_17
from AOCSolver_2021_18 import AOCSolver_2021_18
from AOCSolver_2021_19 import AOCSolver_2021_19
from AOCSolver_2021_20 import AOCSolver_2021_20
from AOCSolver_2021_21 import AOCSolver_2021_21
from AOCSolver_2021_22 import AOCSolver_2021_22
from AOCSolver_2021_23 import AOCSolver_2021_23
from AOCSolver_2021_24 import AOCSolver_2021_24
from AOCSolver_2021_25 import AOCSolver_2021_25
from datetime import datetime


def execute(n, test=False):
    solver = None
    if n == 1:
        solver = AOCSolver_2021_1(n, test)
    elif n == 2:
        solver = AOCSolver_2021_2(n, test)
    elif n == 3:
        solver = AOCSolver_2021_3(n, test)
    elif n == 4:
        solver = AOCSolver_2021_4(n, test)
    elif n == 5:
        solver = AOCSolver_2021_5(n, test)
    elif n == 6:
        solver = AOCSolver_2021_6(n, test)
    elif n == 7:
        solver = AOCSolver_2021_7(n, test)
    elif n == 8:
        solver = AOCSolver_2021_8(n, test)
    elif n == 9:
        solver = AOCSolver_2021_9(n, test)
    elif n == 10:
        solver = AOCSolver_2021_10(n, test)
    elif n == 11:
        solver = AOCSolver_2021_11(n, test)
    elif n == 12:
        solver = AOCSolver_2021_12(n, test)
    elif n == 13:
        solver = AOCSolver_2021_13(n, test)
    elif n == 14:
        solver = AOCSolver_2021_14(n, test)
    elif n == 15:
        solver = AOCSolver_2021_15(n, test)
    elif n == 16:
        solver = AOCSolver_2021_16(n, test)
    elif n == 17:
        solver = AOCSolver_2021_17(n, test)
    elif n == 18:
        solver = AOCSolver_2021_18(n, test)
    elif n == 19:
        solver = AOCSolver_2021_19(n, test)
    elif n == 20:
        solver = AOCSolver_2021_20(n, test)
    elif n == 21:
        solver = AOCSolver_2021_21(n, test)
    elif n == 22:
        solver = AOCSolver_2021_22(n, test)
    elif n == 23:
        solver = AOCSolver_2021_23(n, test)
    elif n == 24:
        solver = AOCSolver_2021_24(n, test)
    elif n == 25:
        solver = AOCSolver_2021_25(n, test)

    solver.solve(1)
    if n != 25:
        solver.solve(2)


t1 = datetime.now()
for i in range(1, 26):
    execute(i, False)
t2 = datetime.now()
print("Total time", t2 - t1)