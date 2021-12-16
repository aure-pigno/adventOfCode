import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_16(AOCSolver):

    data = ""
    binary_data = ""
    pos = 0
    pack = None
    v_map = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

    def parse(self, input):
        self.data = input
        self.decode()
        self.pack , pos = self.parse_packet(0)

    def execute(self, part=1):
        return self.pack.get_versions() if part == 1 else self.pack.compute_value()

    def decode(self):
        for v in helper.split(self.data):
            self.binary_data += self.v_map[v]

    def parse_packet(self, pos):
        p = Packet()
        p.version, pos = self.read_bits(pos, 3)
        p.type, pos = self.read_bits(pos, 3)
        # Literal.
        if p.type == 4:
            p.literal, pos = self.get_literal(pos)
        else:
            p.length_type, pos = self.read_bits(pos, 1)
            if p.length_type == 0:
                packets_length, pos = self.read_bits(pos, 15)
                cur_pos = pos
                while pos < cur_pos + packets_length:
                    np, pos = self.parse_packet(pos)
                    p.subpackets.append(np)
            else:
                subpackets, pos = self.read_bits(pos, 11)
                for i in range(subpackets):
                    np, pos = self.parse_packet(pos)
                    p.subpackets.append(np)
        return p, pos

    def read_bits(self, pos, num):
        n = 0
        for i in range(num):
            n = 2 * n + int(self.binary_data[pos + i])
        return n, pos + num

    def get_literal(self, pos):
        l = 0
        while True:
            g, pos = self.read_bits(pos, 5)
            l = l << 4
            if g & (1 << 4):
                g &= ~(1 << 4)
                l += g
            else:
                l += g
                return (l, pos)


class Packet:
    def __init__(self):
        self.version = None
        self.type = None
        self.literal = None
        self.length_type = None
        self.subpackets = []

    def get_versions(self):
        return self.version + sum([p.get_versions() for p in self.subpackets])

    def compute_value(self):
        if self.type == 4:
            return self.literal

        subvalues = [p.compute_value() for p in self.subpackets]
        if self.type == 0:
            return sum(subvalues)
        elif self.type == 1:
            return helper.multiply_list(subvalues)
        elif self.type == 2:
            return min(subvalues)
        elif self.type == 3:
            return max(subvalues)
        elif self.type == 5:
            return subvalues[0] > subvalues[1]
        elif self.type == 6:
            return subvalues[0] < subvalues[1]
        return subvalues[0] == subvalues[1]