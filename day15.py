# starting_numbers = [0,3,6]
starting_numbers = [2,1,10,11,0,6]

mem = {}
for i in range(len(starting_numbers)):
    mem[starting_numbers[i]] = i

prev = starting_numbers[-1]
prev_new = starting_numbers.count(prev) == 1

for i in range(len(starting_numbers), 30000000):
    n = 0 if prev_new else (i - 1) - mem[prev]
    mem[prev] = i - 1
    prev = n
    prev_new = n not in mem
print(prev)