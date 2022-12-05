def p1():
    with open("input.txt") as f:
        count = 0
        for line in f:
            line = line.strip().split(",")
            line = list(map(lambda x: x.split("-"), line))
            if int(line[0][0]) <= int(line[1][0]) and int(line[0][1]) >= int(
                line[1][1]
            ):
                count += 1
            elif int(line[0][0]) >= int(line[1][0]) and int(line[0][1]) <= int(
                line[1][1]
            ):
                count += 1
        print(count)


def p2():
    with open("input.txt") as f:
        count = 0
        for line in f:
            one, two = line.strip().split(",")
            s1, e1 = one.split("-")
            s2, e2 = two.split("-")
            if not (int(e1) < int(s2) or int(e2) < int(s1)):
                count += 1
        print(count)


p1()
p2()
