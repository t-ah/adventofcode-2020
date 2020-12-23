from collections import deque
from itertools import islice

def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return f.read().split("\n")

def round1(lines):
    p1 = deque([int(x) for x in lines[1:26]])
    p2 = deque([int(x) for x in lines[28:]])

    n_cards = len(p1) * 2
    while abs(len(p1) - len(p2)) != n_cards:
        c1 = p1.popleft()
        c2 = p2.popleft()
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    winner = p1 if len(p1) > 0 else p2
    print(sum([(n_cards - x[0]) * x[1] for x in list(enumerate(winner))]))

def configuration(p1, p2):
    return ",".join([str(x) for x in p1]) + "|" + ",".join([str(x) for x in p2])

def play_game(p1, p2):
    configurations = set()
    while True:
        conf = configuration(p1, p2)
        if conf in configurations:
            return 1
        configurations.add(conf)
        c1 = p1.popleft()
        c2 = p2.popleft()
        if len(p1) >= c1 and len(p2) >= c2:
            round_winner = play_game(deque(islice(p1, 0, c1)), deque(islice(p2, 0, c2)))
        else:
            round_winner = 1 if c1 > c2 else 2
        if round_winner == 1:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
        if len(p1) == 0:
            return 2
        if len(p2) == 0:
            return 1


def main():
    lines = read_input()
    round1(lines)

    p1 = deque([int(x) for x in lines[1:26]])
    p2 = deque([int(x) for x in lines[28:]])
    winner = play_game(p1, p2)
    winner_deck = p1 if winner == 1 else p2
    print(sum([(len(winner_deck) - x[0]) * x[1] for x in list(enumerate(winner_deck))]))

if __name__ == "__main__":
    main()