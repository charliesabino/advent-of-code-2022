def p1():
    with open("input.txt", "r+") as f:
        sum = 0
        for line in f:
            line = line.strip()
            n = len(line) // 2
            line1 = line[0:n]
            line2 = line[n:]
            chars1 = set()
            for char in line1:
                chars1.add(char)
            for char in line2:
                if char in chars1:
                    sum += ord(char) - 96 if char.islower() else ord(char) - 38
                    break
        print(sum)


def p2():
    with open("input.txt", "r+") as f:
        sum = 0
        chars = {}
        for line in f:
            print(chars)
            line = line.strip()
            for char in line:
                chars[char] = chars.get(char, 0) + 1 / \
                    len(re.findall(char, line))
                if chars[char] >= 3:
                    sum += ord(char) - 96 if char.islower() else ord(char) - 38
                    chars = {}
                    break
        print(sum)


p1()
p2()
