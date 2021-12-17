import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_17(AOCSolver):

    def parse(self, input):
        cleaned_input = helper.remove_elems(["target area: ", " ", "x", "y", "="], input.replace("..", ","))
        self.table = [int(v) for v in cleaned_input.split(",")]

    def execute(self, part=1):
        [x_min, x_max, y_min, y_max] = self.table
        total, best_y = 0, 0
        for sx in range(x_max + 1):
            for sy in range(y_min, sx - y_min):
                x, y, max_y, vx, vy = 0, 0, 0, sx, sy
                while x <= x_max and y >= y_min:
                    dx = 0 if vx == 0 else 1 if vx < 0 else -1
                    [x, y, vx, vy] = helper.sum_list([x, y, vx, vy], [vx, vy, dx, -1])
                    max_y = max(y, max_y)
                    if x in range(x_min, x_max + 1) and y in range(y_min, y_max + 1):
                        total += 1
                        best_y = max(best_y, max_y)
                        break
                    elif vx == 0 and x < x_min:
                        break
        return best_y if part == 1 else total
