import math

def count_trees(lines, right, down):
    index = 0
    count = 0
    for i in range(0, len(lines), down):
        line = lines[i]
        if line[index] == "#":
            count += 1
        index = (index + right) % len(line)
    return count


with open("day3.txt", "r") as f:
    lines = f.read().split("\n")

results = [count_trees(lines, *x) for x in [(1,1),(3,1),(5,1),(7,1),(1,2)]]
print(results[1])
print(math.prod(results))