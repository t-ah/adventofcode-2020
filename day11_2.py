def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return [list(x) for x in f.read().split("\n")]


def count_occupied(seats, row, column):
    count = 0
    for dx, dy in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
        y = row
        x = column
        while True:
            y = y + dy
            x = x + dx
            if x < 0 or y < 0 or y >= len(seats) or x >= len(seats[0]):
                break
            seat = seats[y][x]
            if seat == "#":
                count += 1
                break
            if seat == "L":
                break
    return count

def apply_rules(seats):
    new_seats = []
    changes = 0
    for row_i in range(len(seats)):
        new_row = []
        new_seats.append(new_row)
        for col_i in range(len(seats[0])):
            seat = seats[row_i][col_i]
            new_seat = seat
            if seat == "L":
                if count_occupied(seats, row_i, col_i) == 0:
                    new_seat = "#"
                    changes += 1
            elif seat == "#" and count_occupied(seats, row_i, col_i) >= 5:
                new_seat = "L"
                changes += 1
            new_row.append(new_seat)
    return changes, new_seats

def main():
    seats = read_input()

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