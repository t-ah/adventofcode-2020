import re
from math import factorial, prod

def read_input():
    with open(__file__[:5]+".txt", "r") as f:
        return f.read().split("\n")

def calculate(eq):
    while "+" in eq:
        match = re.search(r"\d+ \+ \d+", eq)
        eq_plus_parts = match.group().split(" ")
        repl = str(int(eq_plus_parts[0]) + int(eq_plus_parts[2]))
        eq = eq[:match.span()[0]] + repl + eq[match.span()[1]:]
    factors = [int(x) for x in eq.split(" * ")]
    return prod(factors)

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