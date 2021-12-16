import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_16(AOCSolver):

    binary_data = ""
    pack = None

    def parse(self, input):
        self.binary_data = helper.string_to_hex(input)
        self.pack = self.parse_packet(0)[0]

    def execute(self, part=1):
        return self.pack.get_versions() if part == 1 else self.pack.compute_value()

    def parse_packet(self, pos):
        p = Packet()
        [p.version, pos] = self.read_bits(pos, 3)
        [p.type, pos] = self.read_bits(pos, 3)
        if p.type == 4:
            is_not_last = True
            while is_not_last:
                [is_not_last, pos] = self.read_bits(pos, 1)
                [b, pos] = self.read_bits(pos, 4, False)
                p.literal += b
            return [p, pos]

        [p.length_type, pos] = self.read_bits(pos, 1)
        [length, pos] = self.read_bits(pos, 11 if p.length_type else 15)

        cur_pos, i = pos, 0
        while (not(p.length_type) and pos < cur_pos + length) or (p.length_type and i < length):
            [np, pos] = self.parse_packet(pos)
            p.sub_packets.append(np)
            i += 1
        return [p, pos]

    def read_bits(self, pos, num, number=True):
        v = self.binary_data[pos:(pos + num)]
        return [int("0b" + v, 2) if number else v, (pos + num)]


class Packet:
    def __init__(self):
        self.version = None
        self.type = None
        self.literal = ""
        self.length_type = None
        self.sub_packets = []

    def get_versions(self):
        return self.version + sum([p.get_versions() for p in self.sub_packets])

    def compute_value(self):
        sub_values = [p.compute_value() for p in self.sub_packets]
        if self.type == 0:
            return sum(sub_values)
        elif self.type == 1:
            return helper.multiply_list(sub_values)
        elif self.type == 2:
            return min(sub_values)
        elif self.type == 3:
            return max(sub_values)
        elif self.type == 4:
            return int(self.literal, 2)
        elif self.type == 5:
            return sub_values[0] > sub_values[1]
        elif self.type == 6:
            return sub_values[0] < sub_values[1]
        return sub_values[0] == sub_values[1]
