import re

def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return f.read()

class Tile:
    def __init__(self, id, content, layouts):
        self.id = id
        self.content = content
        self.borders = [Border(self, i, layouts[i]) for i in range(4)]
        self.fixed = False

    def rotate(self):
        self.content = ["".join([line[i] for line in self.content])[::-1] for i in range(len(self.content))]
        temp = self.borders
        self.borders = [temp[3]] + temp[:3]
        for i in range(4):
            self.borders[i].direction = i

    def flip_horizontal(self):
        self.content = [line[::-1] for line in self.content]
        self.borders[1], self.borders[3] = self.borders[3], self.borders[1]
        for i in range(4):
            self.borders[i].layout = self.borders[i].layout[::-1]
            self.borders[i].direction = i

    def flip_vertical(self):
        self.content.reverse()
        self.borders[0], self.borders[2] = self.borders[2], self.borders[0]
        for i in range(4):
            self.borders[i].layout = self.borders[i].layout[::-1]
            self.borders[i].direction = i

class Border:
    def __init__(self, tile, direction, layout):
        self.connected = None
        self.tile = tile
        self.direction = direction
        self.layout = layout

    def connect(self, other_border):
        self.connected = other_border
        other_border.connected = self

def fix_orientations(tile):
    tile.fixed = True
    for direction in range(4):
        border = tile.borders[direction]
        if border.connected == None: continue
        other_border = border.connected
        other_tile = other_border.tile
        if other_tile.fixed: continue

        num_of_rotations = (direction - other_border.direction - 2) % 4
        for _ in range(num_of_rotations):
            other_tile.rotate()
        if other_border.layout == border.layout: # layouts are read in opposite directions
            if direction % 2 == 1:
                other_tile.flip_vertical()
            else:
                other_tile.flip_horizontal()
        fix_orientations(other_tile)

def rotate_lines(lines):
    return ["".join([line[i] for line in lines])[::-1] for i in range(len(lines))]

def flip_lines(lines):
    return list(reversed(lines))

def search_sea_monster(lines):
    # print("Looking for monsters")
    count = 0
    monster = set()
    for i in range(2, len(lines)):
        for match in re.finditer(r"(?=(.#..#..#..#..#..#...))", lines[i]):
            start = match.start(1)
            m = re.match(r"#....##....##....###", lines[i-1][start:])
            if m != None:
                if lines[i-2][start + 18] == "#":
                    s = start
                    monster.update([(i-2,s+18), (i-1,s), (i-1,s+5), (i-1,s+6), (i-1,s+11), (i-1,s+12), (i-1,s+17), (i-1,s+18), (i-1,s+19), (i,s+1), (i,s+4), (i,s+7), (i,s+10), (i,s+13), (i,s+16)])
                    count += 1
    if count > 0:
        # print("\n".join(lines))
        result = sum([line.count("#") for line in lines]) - len(monster)
        print(result)

def main():
    raw_tiles = [x.split("\n") for x in read_input().split("\n\n")]

    borders = {}
    tiles = []
    for tile in raw_tiles:
        tile_id = int(tile[0].split(" ")[1][:-1])
        border_top = tile[1]
        border_bottom = tile[-1][::-1]
        border_left = "".join([line[0] for line in tile if not line.startswith("T")])[::-1]
        border_right = "".join([line[-1] for line in tile if not line.startswith("T")])
        tile_borders = [border_top, border_right, border_bottom, border_left]
        content = [line[1:-1] for line in tile[2:-1]]
        t = Tile(tile_id, content, tile_borders)
        tiles.append(t)
        for tb in t.borders:
            if tb.layout not in borders:
                borders[tb.layout] = tb
                borders[tb.layout[::-1]] = tb
            else:
                other_border = borders[tb.layout]
                tb.connect(other_border)

    prod = 1
    for tile in tiles:
        connected_borders = [b for b in tile.borders if b.connected != None]
        if len(connected_borders) == 2:
            prod *= tile.id
    print(prod)

    fix_orientations(tiles[0])
    
    top_left = tiles[0]
    while top_left.borders[3].connected != None:
        top_left = top_left.borders[3].connected.tile
    while top_left.borders[0].connected != None:
        top_left = top_left.borders[0].connected.tile

    tile_table = [[top_left]]

    tile = top_left
    while tile.borders[2].connected != None:
        tile = tile.borders[2].connected.tile
        tile_table[0].append(tile)
    for x in range(1, len(tile_table[0])):
        tile_table.append([])
        for y in range(len(tile_table[0])):
            left_tile = tile_table[x-1][y]
            tile_table[x].append(left_tile.borders[1].connected.tile)

    lines = []
    for y0 in range(len(tile_table[0])):
        new_lines = tile_table[0][y0].content
        for x in range(1, len(tile_table)):
            tile = tile_table[x][y0]
            for l in range(len(tile.content)):
                new_lines[l] += tile.content[l]
        lines += new_lines

    for _ in range(4):
        lines = rotate_lines(lines)
        search_sea_monster(lines)
    lines = flip_lines(lines)
    for _ in range(4):
        lines = rotate_lines(lines)
        search_sea_monster(lines)

if __name__ == "__main__":
    main()