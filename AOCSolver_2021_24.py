import helper
from AOCSolver import AOCSolver
import functools


class AOCSolver_2021_24(AOCSolver):

    add_x, div_z, add_y = [], [], []
    max_zs = 0

    def parse(self, input):
        for line_number, line in enumerate(input.split("\n")):
            if "add x " in line and "add x z" not in line:
                self.add_x.append(int(line.split()[2]))
            if "div z " in line:
                self.div_z.append(int(line.split()[2]))
            if "add y " in line and line_number % 18 == 15:
                self.add_y.append(int(line.split()[2]))
        self.max_zs = [26 ** len([x for x in range(len(self.div_z)) if self.div_z[x] == 26 and x >= i])
                      for i in range(len(self.div_z))]

    def execute(self, part=1):
        model_numbers = [int(x) for x in self.compute(0, 0)]
        return max(model_numbers) if part == 1 else min(model_numbers)

    @functools.lru_cache(maxsize=None)
    def compute(self, batch, current_z):
        if batch == 14 or current_z > self.max_zs[batch]:
            return [""] if current_z == 0 else []
        next_x, next_y = self.compute_x(batch, current_z), self.compute_y(batch, current_z)

        ret = []
        for w in [next_x] if next_x in range(1, 10) else list(range(1, 10)):
            for x in self.compute(batch + 1, self.compute_z(batch, next_x, next_y, current_z, w)):
                ret.append(str(w) + x)
        return ret

    def compute_x(self, batch, z):
        return self.add_x[batch] + (z % 26)

    def compute_y(self, batch, z):
        return self.add_y[batch] + (z * 26)

    def compute_z(self, batch, x, y, z, w):
        z = int(z / self.div_z[batch])
        return z if x == w else w + y

# A batch is always 18 lines
# X and Y are always 0 at the end of a batch
# Sequence per batch is always the same
