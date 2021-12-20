import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_20(AOCSolver):
    image = []
    enhancer = []

    def parse(self, input):
        self.table = input.replace(".","0").replace("#","1").split("\n")
        self.enhancer = helper.split_convert(self.table[0])
        for elem in self.table[2:]:
            self.image.append(helper.split_convert(elem))

    def execute(self, part=1):
        it = 2 if part == 1 else 50
        t = helper.copy_table(self.image)
        pixels = set()
        for i, row in enumerate(t):
            for j, col in enumerate(row):
                if col == 1:
                    pixels.add((i, j))

        for i in range(it):
            pixels = self.process_image(pixels, i)
        return len(pixels)

    def process_image(self, pixels, step):

        min_row, max_row, min_col, max_col = float('inf'), 0, float('inf'), 0
        light_pixels = set()
        for pixel in pixels:
            min_row, max_row = min(min_row, pixel[0]), max(max_row, pixel[0])
            min_col, max_col = min(min_col, pixel[1]), max(max_col, pixel[1])

        for i in range(min_row - 1, max_row + 2):
            for j in range(min_col - 1, max_col + 2):
                number = 0
                for i1 in range(i - 1, i + 2):
                    for j1 in range(j - 1, j + 2):
                        if min_row <= i1 <= max_row and min_col <= j1 <= max_col:
                            number = 2 * number + ((i1, j1) in pixels)
                        else:
                            number = 2 * number + (step % 2)
                if self.enhancer[number]:
                    light_pixels.add((i, j))
        return light_pixels
