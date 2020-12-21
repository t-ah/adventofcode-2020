from collections import defaultdict

def read_input():
    with open(__file__[:5]+".txt", "r") as f:
        return f.read().split("\n")

def neighbours(x,y,z,w):
    d = (-1,0,1)
    for dx in d:
        for dy in d:
            for dz in d:
                for dw in d:
                    yield (x+dx,y+dy,z+dz,w+dw)

def count_active_neighbours(xyz, blocks):
    count = -1 if blocks[xyz] else 0
    for other_xyz in neighbours(*xyz):
        if blocks[other_xyz]:
            count += 1
    return count

def cycle(blocks):
    new_blocks = defaultdict(bool)
    for xyz in list(blocks):
        for block in neighbours(*xyz):
            if block in new_blocks: continue
            active_neighbours = count_active_neighbours(block, blocks)
            if (blocks[block] and active_neighbours in (2,3)) or (not blocks[block] and active_neighbours == 3):
                new_blocks[block] = True
    return new_blocks

def main():
    lines = read_input()
    blocks = defaultdict(bool)
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            if line[x] == "#":
                blocks[x,y,0,0] = True
    for _ in range(6):
        blocks = cycle(blocks)
    print(len(blocks))

if __name__ == "__main__":
    main()