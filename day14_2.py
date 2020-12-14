def read_input():
    with open(__file__[:5]+".txt", "r") as f:
        return [x.split(" = ") for x in f.read().split("\n")]

def apply_mask(s, mask):
    res = [c for c in mask]
    for i in range(len(res)):
        if res[i] == "X": res[i] = s[i]
    return "".join(res)

def to_bit_str(n):
    return format(int(n), '036b')

def bit_str_to_int(bit_str):
    return int(bit_str, base=2)

def main():
    lines = read_input()
    mem = {}
    mask = ""
    for line in lines:
        if line[0] == "mask":
            mask = line[1]
        else:
            addr = line[0][4:-1]
            bit_str = to_bit_str(line[1])
            masked_bit_str = apply_mask(bit_str, mask)
            mem[addr] = masked_bit_str
    print(sum([bit_str_to_int(x) for x in mem.values()]))

if __name__ == "__main__":
    main()