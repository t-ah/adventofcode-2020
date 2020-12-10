def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return f.read().split("\n")

def find_problem(numbers):
    sliding_set = set()
    sliding_set.update(numbers[:25])
    
    for i in range(25, len(numbers)):
        n = numbers[i]
        found = False
        for s1 in sliding_set:
            s2 = n - s1
            if s2 != s1 and s2 in sliding_set:
                found = True
                break
        if not found:
            return numbers[i]
        sliding_set.remove(numbers[i - 25])
        sliding_set.add(n)

def main():
    numbers = [int(x) for x in read_input()]
    target = find_problem(numbers)
    print(target) # part 1

    sliding_sum = numbers[0]
    first_index = 0
    last_index = 0
    while True:
        if sliding_sum < target:
            last_index += 1
            sliding_sum += numbers[last_index]
        elif sliding_sum > target:
            sliding_sum -= numbers[first_index]
            first_index += 1
        else:
            series = numbers[first_index:last_index + 1]
            print(min(series) + max(series))
            break


if __name__ == "__main__":
    main()