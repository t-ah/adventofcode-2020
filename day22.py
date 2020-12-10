def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return f.read().split("\n")

def main():
    lines = read_input()

if __name__ == "__main__":
    main()