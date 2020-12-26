def find_loop_size(subj, result):
    v = 1
    i = 0
    while True:
        i += 1
        v = transform(v, subj)
        if v == result:
            return i

def transform(val, subj):
    val *= subj
    return val % 20201227

def main():
    card = 1327981
    door = 2822615

    l = find_loop_size(7, card)
    print(transform(door, l))

if __name__ == "__main__":
    main()