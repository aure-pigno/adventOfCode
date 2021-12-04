def execute(input, part=1):
    x, y1, y2 = 0, 0, 0
    comp = lambda k, v: [x + v * (k == "forward"), y1 + v * y2 * (k == "forward"), y2 + v * ((k == "down") - (k == "up"))]
    for line in input:
        [k, v] = line.split(" ")
        [x, y1, y2] = comp(k, int(v))
    return x * y1 if part == 1 else x * y2