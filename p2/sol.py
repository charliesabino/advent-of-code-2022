def p1():
    with open('input.txt') as f:


def p2():
    with open("input.txt", "r+") as f:
        wins = {"A": "Y", "B": "Z", "C": "X"}
        ties = {"A": "X", "B": "Y", "C": "Z"}
        lose = {"A": "Z", "B": "X", "C": "Y"}
        scores = {"X": 1, "Y": 2, "Z": 3}
        score = 0
        for line in f:
            line = list(line.split())
            if line[1] == "X":
                move = lose[line[0]]
                score += scores[move]
            elif line[1] == "Y":
                move = ties[line[0]]
                score += scores[move] + 3
            else:
                move = wins[line[0]]
                score += scores[move] + 6
        print(score)
