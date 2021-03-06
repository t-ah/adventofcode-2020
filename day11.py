def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return [list(x) for x in f.read().split("\n")]


def count_occupied(seats, row, column):
    count = 0
    for dx, dy in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
        if seats[row + dx][column + dy] == "#":
            count += 1
    return count

def apply_rules(seats):
    new_seats = []
    changes = 0
    for row_i in range(1, len(seats) - 1):
        new_row = []
        new_seats.append(new_row)
        for col_i in range(1, len(seats[0]) - 1):
            seat = seats[row_i][col_i]
            new_seat = seat
            if seat == "L":
                if count_occupied(seats, row_i, col_i) == 0:
                    new_seat = "#"
                    changes += 1
            elif seat == "#" and count_occupied(seats, row_i, col_i) >= 4:
                new_seat = "L"
                changes += 1
            new_row.append(new_seat)
    add_padding(new_seats)
    return changes, new_seats

def add_padding(seats):
    width = len(seats[0])
    seats.insert(0, ["."] * width)
    seats.append(["."] * width)
    for row in seats:
        row.insert(0, ".")
        row.append(".")

def main():
    seats = read_input()
    add_padding(seats)

    while True:
        changes, seats = apply_rules(seats)
        print(changes)
        if changes == 0:
            break

    occupied = 0
    for row in seats:
        occupied += row.count("#")
    print(occupied)

if __name__ == "__main__":
    main()