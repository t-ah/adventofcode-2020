def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return f.read().split("\n")


def move(pos, dir, distance):
    for i in [0,1]:
        pos[i] += distance * dir[i]

def rotate(wp, times, clockwise):
    for _ in range(times):
        y, x = wp
        wp[0] = x
        wp[1] = y
        wp[0 if clockwise else 1] *= -1


def main():
    instructions = [[x[:1], int(x[1:])] for x in read_input()]

    directions = ((1,0), (0,1), (-1,0), (0,-1)) # clockwise, starting with E
    dir_index = 0
    pos = [0,0]

    for instr in instructions:
        if instr[0] == "F":
            move(pos, directions[dir_index], instr[1])
        elif instr[0] == "N":
            move(pos, directions[3], instr[1])
        elif instr[0] == "E":
            move(pos, directions[0], instr[1])
        elif instr[0] == "S":
            move(pos, directions[1], instr[1])
        elif instr[0] == "W":
            move(pos, directions[2], instr[1])
        elif instr[0] == "R":
            dir_index = (dir_index + instr[1]//90) % len(directions)
        elif instr[0] == "L":
            dir_index = (dir_index - instr[1]//90) % len(directions)

    print(abs(pos[0]) + abs(pos[1]))


    pos = [0,0]
    wp = [10, -1]

    for instr in instructions:
        if instr[0] == "F":
            for i in (0,1): pos[i] += instr[1] * wp[i]
        elif instr[0] == "N":
            move(wp, directions[3], instr[1])
        elif instr[0] == "E":
            move(wp, directions[0], instr[1])
        elif instr[0] == "S":
            move(wp, directions[1], instr[1])
        elif instr[0] == "W":
            move(wp, directions[2], instr[1])
        else: # R/L
            rotate(wp, instr[1]//90, instr[0]=="R")

    print(abs(pos[0]) + abs(pos[1]))


if __name__ == "__main__":
    main()