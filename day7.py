from collections import defaultdict

def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return f.read().split("\n")

def count_color(color, map):
    count = 0
    color_map = map[color]
    if len(color_map) == 0:
        return 1
    for contained_color in color_map:
        count += color_map[contained_color] * count_color(contained_color, map)
    return count + 1 # count the bag itself

def main():
    color_maps = defaultdict(lambda: defaultdict(int))
    may_contain = defaultdict(lambda: set())
    lines = read_input()
    for line in lines:
        words = line.split(" ")
        color = f"{words[0]} {words[1]}"
        for i in range(4, len(words), 4):
            qty = words[i]
            if qty != "no":
                other_color = f"{words[i+1]} {words[i+2]}"
                color_maps[color][other_color] = int(qty)
                may_contain[other_color].add(color)

    colors = set()
    colors.add("shiny gold")
    while True:
        old_size = len(colors)
        new_colors = set()
        for c in colors:
            new_colors.update(may_contain[c])
        colors.update(new_colors)
        if len(colors) == old_size:
            break
    print(len(colors) - 1)

    result = count_color("shiny gold", color_maps)
    print(result - 1)

if __name__ == "__main__":
    main()