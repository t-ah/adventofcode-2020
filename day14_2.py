import itertools

def read_input():
    with open(__file__[:5]+".txt", "r") as f:
        return [x.split(" = ") for x in f.read().split("\n")]

def to_bit_str(n):
    return format(int(n), '036b')

def bit_str_to_int(bit_str):
    return int(bit_str, base=2)

# TODO: there must be a better approach
def get_addresses(addr, mask):
    bit_str = to_bit_str(addr)
    res = []
    bit_arr = [c for c in bit_str]
    floating = []
    for i in range(len(mask)):
        if mask[i] == "X":
            floating.append(i)
        elif mask[i] == "1":
            bit_arr[i] = "1"
    combinations = list(itertools.product([0, 1], repeat=len(floating)))
    for combi in combinations:
        for i in range(len(combi)):
            index = floating[i]
            bit_arr[index] = str(combi[i])
        res.append("".join(bit_arr))
    return res

def main():
    lines = read_input()
    mem = {}
    mask = ""
    for line in lines:
        if line[0] == "mask":
            mask = line[1]
        else:
            addresses = get_addresses(line[0][4:-1], mask)
            for a in addresses:
                mem[a] = int(line[1])
    print(sum(mem.values()))

if __name__ == "__main__":
    main()