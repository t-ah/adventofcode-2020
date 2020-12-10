def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return f.read().split("\n")

def terminates(instructions):
    acc = 0
    pc = 0
    pcs = set()

    while True:
        if pc == len(instructions):
            return True, acc
        if pc in pcs:
            return False, acc

        pcs.add(pc)
        instr = instructions[pc]
        if instr[0] == "acc":
            acc += instr[1]
            pc += 1
        elif instr[0] == "jmp":
            pc += instr[1]
        elif instr[0] == "nop":
            pc += 1

def main():
    instructions = [(x[0], int(x[1])) for x in [x.split(" ") for x in read_input()]]
    print(terminates(instructions)[1]) # part 1

    for i in range(len(instructions)):
        current_instr = instructions[i]
        if current_instr[0] == "nop":
            instructions[i] = ("jmp", current_instr[1])
        elif current_instr[0] == "jmp":
            instructions[i] = ("nop", current_instr[1])
        else:
            continue
        terminated, acc = terminates(instructions)
        if terminated:
            print(acc) # part 2
            break
        instructions[i] = current_instr

if __name__ == "__main__":
    main()