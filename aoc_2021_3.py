def get_bit_map(i, t):
    mp = {"0": [], "1": []}
    for elem in t:
        mp[elem[i]].append(elem)
    return mp


def get_record(records, ox=True):
    for i in range(0, len(records[0])):
        hmap = get_bit_map(i, records)
        num = int(len(hmap["1"]) >= len(hmap["0"]))
        records = hmap[str(num if ox else 1 - num)]
        if len(records) == 1:
            return int(records[0], 2)


def execute(input, part=1):
    if part == 1:
        gamma, epsilon = "", ""
        for i in range(0, len(input[0])):
            elem = get_bit_map(i, input)
            v = int(len(elem["1"]) > len(elem["0"]))
            epsilon += str(v)
            gamma += str(1 - v)
        return int(epsilon, 2) * int(gamma, 2)
    return get_record(input) * get_record(input, False)
