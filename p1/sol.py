def p1():
    with open("input.txt", "r+") as f:
        tot = []
        cur = []
        for line in f:
            line = line.strip()
            if line == "":
                tot.append(cur)
                cur = []
            else:
                cur.append(int(line))
        print(max(map(sum, tot)))


def p2():
    with open("input.txt", "r+") as f:
        tot = []
        cur = []
        for line in f:
            line = line.strip()
            if line == "":
                tot.append(cur)
                cur = []
            else:
                cur.append(int(line))
        tot = list((map(sum, tot)))
        tot.sort()
        print(tot[-1] + tot[-2] + tot[-3])


p1()
p2()
