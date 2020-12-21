import re

def read_input():
    with open(__file__[:5]+".txt", "r") as f:
        return f.read().split("\n")

def calculate(eq):
    # no paranth.
    parts = eq.split(" ")
    res = int(parts[0])
    for i in range(1, len(parts), 2):
        if parts[i] == "+":
            res += int(parts[i+1])
        else:
            res *= int(parts[i+1])
    return res


def evaluate(eq):
    while "(" in eq:
        exprs = re.findall(r"\([\d\s\+\*]+\)", eq)
        for expr in exprs:
            eq = eq.replace(expr, str(calculate(expr[1:-1])))
    return calculate(eq)

def main():
    lines = read_input()
    results = [evaluate(line) for line in lines]
    print(sum(results))

if __name__ == "__main__":
    main()