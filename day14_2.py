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
            print(pow(2, mask.count("X")))
        else:
            pass

if __name__ == "__main__":
    main()