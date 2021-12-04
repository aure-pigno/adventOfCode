def execute(input, depth=1):
    return sum([(sum(input[(i + 1):(i + 1) + depth]) > sum(input[i:i + depth])) for i in range(0, len(input) - (depth - 1))])
