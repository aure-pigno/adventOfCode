def split(word):
    return [char for char in word]

def table_converter(text_table):
    return [int(i) for i in text_table]

def f_2021day3_getBitMap(i, t):
    mp = {"0": [], "1": []}
    for elem in t:
        mp[elem[i]].append(elem)
    return mp

def f_2021day3_getRecord(records, ox = True):
    for i in range(0, len(records[0])):
        hmap = f_2021day3_getBitMap(i, records)
        num = int(len(hmap["1"]) >= len(hmap["0"]))
        records = hmap[str(num if ox else 1-num)]
        if len(records) == 1:
            return int(records[0], 2)
