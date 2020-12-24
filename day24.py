from collections import Counter

def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return f.read().split("\n")

def neighbours(x,y):
    return {(x-1,y), (x+1,y), (x,y-1), (x+1,y-1), (x-1,y+1), (x,y+1)}

def step(black_tiles):
    new_tiles = set()
    relevant_tiles = set().union(*[neighbours(*t) for t in black_tiles], black_tiles)
    for t in relevant_tiles:
        n = len(neighbours(*t).intersection(black_tiles))
        if t in black_tiles:
            if n == 1 or n == 2:
                new_tiles.add(t)
        else:
            if n == 2:
                new_tiles.add(t)
    return new_tiles

def main():
    lines = read_input()
    tiles = Counter()
    for line in lines:
        prev = ""
        x, y = 0, 0
        for c in line:
            if c == "w":
                if prev != "n":
                    x -= 1
            elif c == "e":
                if prev != "s":
                    x += 1
            if prev == "n":
                y -= 1
            elif prev == "s":
                y += 1
            prev = c
        tiles[(x,y)] += 1
    
    black_tiles = set()
    for tile, flip_count in tiles.items():
        if flip_count % 2 == 1:
            black_tiles.add(tile)
    print(len(black_tiles))


    for _ in range(100):
        black_tiles = step(black_tiles)
    print(len(black_tiles))

if __name__ == "__main__":
    main()