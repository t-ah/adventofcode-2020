# for part 2: day19_2.txt (manually transformed into CNF)
from collections import defaultdict

def read_input():
    with open(__file__.replace(".py", ".txt"), "r") as f:
        return f.read()

def parse_rules(text):
    rules = {}
    for line in text.split("\n"):
        lhs, rhs = line.split(": ")
        rhs = rhs.split(" | ")
        conclusio = []
        for vars in rhs:
            if vars[0] == '"':
                vars = [vars[1]]
            else:
                vars = vars.split(" ")
            conclusio.append(vars)
        rules[lhs] = conclusio
    return rules

def fix_CNF(rules):
    for lhs in rules:
        c = rules[lhs]
        for vars_list in list(c):
            if len(vars_list) == 1:
                var = vars_list[0]
                if var == "a" or var == "b":
                    continue
                # print(f"{c} remove {vars_list}")
                c.remove(vars_list)
                chained_rhs = rules[var]
                for rhs in chained_rhs:
                    # print(f"{c} append {rhs}")
                    c.append(rhs)

def cyk(word, rules, inverted_rules):
    print(word)
    n = len(word)
    # T = [[set([]) for j in range(n)] for i in range(n)]

    # for j in range(0, n):
    #     for lhs, conclusio in rules.items():
    #         for rhs in conclusio:
    #             if len(rhs) == 1 and rhs[0] == word[j]:
    #                 T[j][j].add(lhs)

    #     for i in range(j, -1, -1):
    #         for k in range(i, j + 1):
    #             for lhs, conclusio in rules.items():
    #                 for rhs in conclusio:
    #                     if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k + 1][j]:
    #                         T[i][j].add(lhs)
    # return len(T[0][n-1]) != 0

    table = defaultdict(lambda: set())
    # start with diagonal
    for i in range(n):
        for lhs, rhs in rules.items():
            for production in rhs:
                if len(production) == 1 and production[0] == word[i]:
                    table[(i,i)].add(lhs)
    for iteration in range(1, n):
        for i in range(n - iteration):
            j = iteration + i
            # if i == 0 and j == n-1: print(f"cell({i},{j})")
            max_offset = iteration
            for offset in range(1, max_offset + 1):
                c_j = j - offset
                c_i = i + max_offset + 1 - offset
                # if i == 0 and j == n-1: print(f"check {i} {c_j} and {c_i} {j}")
                t_1 = table[(i, c_j)]
                t_2 = table[(c_i, j)]
                for var_1 in t_1:
                    for var_2 in t_2:
                        lookup = (var_1, var_2)
                        if lookup in inverted_rules:
                            table[(i,j)].update(inverted_rules[lookup])
    return "0" in table[(0, n-1)]

def main():
    texts = read_input().split("\n\n")

    rules = parse_rules(texts[0])
    fix_CNF(rules)

    inverted_rules = defaultdict(lambda: set())
    for lhs, productions in rules.items():
        for p in productions:
            if len(p) == 2:
                key = (p[0], p[1])
                inverted_rules[key].add(lhs)

    l = [x for x in texts[1].split("\n") if cyk(x, rules, inverted_rules)]
    print(len(l))

if __name__ == "__main__":
    main()