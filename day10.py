from math import prod
import itertools

def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return f.read().split("\n")

def count_possibilities(n, cache):
    if n in cache:
        return cache[n]
    combinations = list(itertools.product([0, 1], repeat=n))
    count = 0
    for c in combinations:
        if "000" not in "".join(map(str,c)):
            count += 1
    cache[n] = count
    return count

def main():
    jolts = [0] + sorted([int(x) for x in read_input()])
    jolts.append(jolts[-1] + 3)
    count1 = 0
    count3 = 0
    chains = []
    current_chain = 0
    for i in range(len(jolts) - 1):
        if jolts[i + 1] - jolts[i] == 1:
            count1 += 1
            current_chain += 1
        elif jolts[i + 1] - jolts[i] == 3:
            count3 += 1
            if current_chain > 1:
                chains.append(current_chain - 1)
            current_chain = 0
    print(count1 * count3)

    cache = {}
    chain_possibilities = [count_possibilities(n, cache) for n in chains]
    print(prod(chain_possibilities))

if __name__ == "__main__":
    main()