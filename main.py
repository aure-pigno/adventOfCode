from AOCSolver_2021_1 import AOCSolver_2021_1
from AOCSolver_2021_2 import AOCSolver_2021_2
from AOCSolver_2021_3 import AOCSolver_2021_3
from AOCSolver_2021_4 import AOCSolver_2021_4
from AOCSolver_2021_5 import AOCSolver_2021_5
from AOCSolver_2021_6 import AOCSolver_2021_6


def execute(n):
    solver = None
    if n == 1:
        solver = AOCSolver_2021_1(n)
    elif n == 2:
        solver = AOCSolver_2021_2(n)
    elif n == 3:
        solver = AOCSolver_2021_3(n)
    elif n == 4:
        solver = AOCSolver_2021_4(n)
    elif n == 5:
        solver = AOCSolver_2021_5(n)
    elif n == 6:
        solver = AOCSolver_2021_6(n)
    else:
        print("---")
        print("Day", n, "not implemented yet")
        return
    solver.solve(1)
    solver.solve(2)


for i in range(1,6):
    execute(i)
