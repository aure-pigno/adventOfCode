import helper
from AOCSolver import AOCSolver
import itertools
import math
from functools import reduce

class AOCSolver_2021_18(AOCSolver):

    def parse(self, input):
        self.table = list(map(eval, input.split("\n")))

    def execute(self, part=1):
        t = helper.copy_table(self.table)
        if part == 1:
            return self.magnitude(reduce(self.add, t))
        return max(self.magnitude(self.add(a, b)) for a, b in itertools.permutations(t, 2))

    def magnitude(self, x):
        return x if isinstance(x, int) else 3 * self.magnitude(x[0]) + 2 * self.magnitude(x[1])

    def add(self, a, b):
        x = [a, b]
        while True:
            change, _, x, _ = self.explode(x)
            if not change:
                change, x = self.split(x)
                if not change:
                    break
        return x

    def split(self, x):
        if isinstance(x, int):
            v = x if x < 10 else [int(x / 2), math.ceil(x / 2)]
            return x >= 10, v
        a, b = x
        change, a = self.split(a)
        if not change:
            change, b = self.split(b)
        return change, [a, b]

    def explode(self, x, n=4):
        if isinstance(x, int):
            return False, None, x, None
        if n == 0:
            return True, x[0], 0, x[1]
        a, b = x
        exp, left, a, right = self.explode(a, n - 1)
        if exp:
            return True, left, [a, self.add_dir(b, right, True)], None
        exp, left, b, right = self.explode(b, n - 1)
        if exp:
            return True, None, [self.add_dir(a, left, False), b], right
        return False, None, x, None

    def add_dir(self, x, n, is_left=True):
        if n is None:
            return x
        if isinstance(x, int):
            return x + n
        a = self.add_dir(x[0], n, is_left) if is_left else x[0]
        b = x[1] if is_left else self.add_dir(x[1], n, is_left)
        return [a, b]