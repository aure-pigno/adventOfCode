def execute(input, depth=1):
    count = 0
    for i in range(0, len(input) - (depth - 1)):
        count += (sum(input[(i + 1):(i + 1) + depth]) > sum(input[i:i + depth]))
    return count