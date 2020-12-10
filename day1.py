with open("day1.txt", "r") as f:
    numbers = set([int(x) for x in f.readlines()])

for n in numbers:
    if 2020 - n in numbers:
        print(n * (2020 - n))
        break

while len(numbers) > 0:
    n1 = numbers.pop()
    for n2 in numbers:
        n3 = 2020 - n1 - n2
        if n1 == n3 or n2 == n3:
            continue
        if n3 in numbers:
            print(n1 * n2 * n3)
            numbers.clear()
            break