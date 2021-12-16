import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_16(AOCSolver):

    binary_data = ""
    pack = None
    v_map = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

    def parse(self, input):
        self.binary_data = "".join([self.v_map[v] for v in helper.split(data)])
        self.pack = self.parse_packet(0)[0]

    def execute(self, part=1):
        return self.pack.get_versions() if part == 1 else self.pack.compute_value()

    def parse_packet(self, pos):
        p = Packet()
        [p.version, pos] = self.read_bits(pos, 3)
        [p.type, pos] = self.read_bits(pos, 3)
        if p.type == 4:
            [p.literal, pos] = self.get_literal(pos)
            return [p, pos]

        [p.length_type, pos] = self.read_bits(pos, 1)
        [packets_length, pos] = self.read_bits(pos, 11 if p.length_type else 15)

        cur_pos, i = pos, 0
        while (not(p.length_type) and pos < cur_pos + packets_length) or (p.length_type and i < packets_length):
            [np, pos] = self.parse_packet(pos)
            p.sub_packets.append(np)
            i += 1
        return [p, pos]

    def read_bits(self, pos, num, number=True):
        if number:
            return [int("0b" + self.binary_data[pos:(pos + num)], 2), (pos + num)]
        return [self.binary_data[pos:(pos + num)], (pos + num)]

    def get_literal(self, pos):
        is_not_last, v = True, ""
        while is_not_last:
            [is_not_last, pos] = self.read_bits(pos, 1)
            [b, pos] = self.read_bits(pos, 4, False)
            v += b
        return [int(v, 2), pos]


class Packet:
    def __init__(self):
        self.version = None
        self.type = None
        self.literal = None
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
            return self.literal
        elif self.type == 5:
            return sub_values[0] > sub_values[1]
        elif self.type == 6:
            return sub_values[0] < sub_values[1]
        return sub_values[0] == sub_values[1]
