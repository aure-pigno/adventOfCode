import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_6(AOCSolver):
    table = []

    def parse(self, input):
        self.table = input.split("\n")

    def execute(self, part=1):
        return part