import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_20(AOCSolver):
    image = []
    enhanced = []
    def parse(self, input):
        self.table = input.replace(".","0").replace("#","1").split("\n")
        print(self.table)
        for i in range(len(self.table)):
            if i == 0:
                self.enhanced = [int(v) for v in helper.split(self.table[i])]
            elif i != 1:
                self.image.append([int(v) for v in helper.split(self.table[i])])

    def execute(self, part=1):
        it = 2 if part == 1 else 50
        t = helper.copy_table(self.image)
        light_pixels = set()
        for i, row in enumerate(t):
            for j, col in enumerate(row):
                if col == 1:
                    light_pixels.add((i, j))
        frozen_light_pixels = frozenset(light_pixels)

        for i in range(it):
            frozen_light_pixels = self.process_image(frozen_light_pixels, i)
        return len(frozen_light_pixels)

    def process_image(self, light_pixels, step):
        min_row, max_row, min_col, max_col = float('inf'), 0, float('inf'), 0
        for pixel in light_pixels:
            min_row, max_row = min(min_row, pixel[0]), max(max_row, pixel[0])
            min_col, max_col = min(min_col, pixel[1]), max(max_col, pixel[1])
        lights = set()

        for i in range(min_row - 3, max_row + 4):
            for j in range(min_col - 3, max_col + 4):
                number = 0
                for i1 in range(i - 1, i + 2):
                    for j1 in range(j - 1, j + 2):
                        if min_row <= i1 <= max_row and min_col <= j1 <= max_col:
                            number = 2 * number + ((i1, j1) in light_pixels)
                        else:
                            number = 2 * number + (step % 2)
                if self.enhanced[number]:
                    lights.add((i, j))
        return lights
