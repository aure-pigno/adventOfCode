import helper
from AOCSolver import AOCSolver


class AOCSolver_2021_16(AOCSolver):

    data = ""
    pos = 0
    pack = None

    def parse(self, input):
        self.data = input
        self.pack , pos = self.parse_packet(0)

    def execute(self, part=1):
        return self.pack.get_versions() if part == 1 else self.pack.compute_value()

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

    def get_bit(self, pos):
        char = int(pos / 4)
        bit = 3 - (pos % 4)
        return (int(self.data[char], 16) & (1 << bit)) >> bit

    def read_bits(self, pos, num):
        n = 0
        for i in range(num):
            n = 2 * n + self.get_bit(pos + i)
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
        return self.version + sum([p.add_versions() for p in self.subpackets])

    def compute_value(self):
        if self.type == 4:
            return self.literal

        subvalues = [p.calculate_value() for p in self.subpackets]
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