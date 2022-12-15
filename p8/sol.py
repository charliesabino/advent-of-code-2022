def p1():
    with open("input.txt") as f:
        grid = []
        count = 0
        for line in f:
            line = list(line.strip())
            line = [int(x) for x in line]
            grid.append(line)
        print(grid)
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if is_visible(grid, i, j):
                    count += 1
        count += len(grid) * 2 + len(grid[0]) * 2 - 4
        print(count)


def p2():
    with open("input.txt") as f:
        grid = []
        max_score = 0
        for line in f:
            line = list(line.strip())
            line = [int(x) for x in line]
            grid.append(line)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                score = get_score(grid, i, j)
                if score > max_score:
                    max_score = score
        print(max_score)


def is_visible(grid, i, j):
    neighbors = []
    for r in range(0, i):
        neighbors.append(grid[r][j])
    if len(list(filter(lambda x: x >= grid[i][j], neighbors))) == 0:
        return True
    neighbors = []
    for r in range(i + 1, len(grid)):
        neighbors.append(grid[r][j])
    if len(list(filter(lambda x: x >= grid[i][j], neighbors))) == 0:
        return True
    neighbors = []
    for c in range(0, j):
        neighbors.append(grid[i][c])
    if len(list(filter(lambda x: x >= grid[i][j], neighbors))) == 0:
        return True
    neighbors = []
    for c in range(j + 1, len(grid[0])):
        neighbors.append(grid[i][c])
    if len(list(filter(lambda x: x >= grid[i][j], neighbors))) == 0:
        return True
    return False


def get_score(grid, i, j):
    score = 1
    count = 0
    for r in range(i - 1, -1, -1):
        tree = grid[r][j]
        count += 1
        if tree >= grid[i][j]:
            score *= count
            count = 0
            break
    if count > 0:
        score *= count
        count = 0
    for r in range(i + 1, len(grid)):
        tree = grid[r][j]
        count += 1
        if tree >= grid[i][j]:
            score *= count
            count = 0
            break
    if count > 0:
        score *= count
        count = 0
    for c in range(j - 1, -1, -1):
        tree = grid[i][c]
        count += 1
        if tree >= grid[i][j]:
            score *= count
            count = 0
            break
    if count > 0:
        score *= count
        count = 0
    for c in range(j + 1, len(grid[0])):
        tree = grid[i][c]
        count += 1
        if tree >= grid[i][j]:
            score *= count
            count = 0
            break
    if count > 0:
        score *= count
        count = 0
    return score


p1()
p2()
