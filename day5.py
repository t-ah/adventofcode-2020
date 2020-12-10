def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return f.read().split("\n")

def find_seat(start, front_letter, directions):
    width = start // 2 + 1
    for c in directions:
        if c == front_letter:
            start -= width
        width //= 2
    return start

def main():
    seats = read_input()
    all_ids = []
    for seat in seats:
        row = find_seat(127, "F", seat[:7])
        column = find_seat(7, "L", seat[7:])
        id = 8 * row + column
        all_ids.append(id)
    all_ids.sort()

    print(all_ids[-1])

    for i in range(len(all_ids) - 1):
        if all_ids[i + 1] == all_ids[i] + 2:
            print(all_ids[i] + 1)
            break

if __name__ == "__main__":
    main()