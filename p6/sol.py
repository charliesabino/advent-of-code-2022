def p1():
    with open("input.txt") as f:
        for line in f:
            for i in range(len(line)):
                chars = set(line[i: i + 14])
                if len(chars) == 14:
                    return i + 14
    return i


print(p1())
