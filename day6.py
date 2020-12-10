import string

def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return [x.split("\n") for x in f.read().split("\n\n")]

def main():
    count = 0
    count2 = 0
    groups = read_input()
    for group in groups:
        one_yes = set()
        all_yes = set()
        all_yes.update(list(string.ascii_lowercase))
        for answer in group:
            chars = list(answer)
            one_yes.update(chars)
            all_yes = all_yes.intersection(chars)
        count += len(one_yes)
        count2 += len(all_yes)
    print(count)
    print(count2)

if __name__ == "__main__":
    main()