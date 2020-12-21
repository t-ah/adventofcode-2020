from collections import defaultdict, Counter

def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return f.read().split("\n")

def main():
    lines = read_input()

    possible_ingredients = defaultdict(lambda: list())
    ingr_count = Counter()

    for line in lines:
        parts = line.split(" (contains ")
        ingredients = parts[0].split(" ")
        for i in ingredients:
            ingr_count[i] += 1
        allergens = parts[1].split(", ")
        allergens[-1] = allergens[-1][:-1]
        # print(ingredients)
        # print(allergens)
        ingr_set = set()
        ingr_set.update(ingredients)
        for a in allergens:
            possible_ingredients[a].append(ingr_set)
    

    for allergen in list(possible_ingredients):
        possible_ingredients[allergen] = set.intersection(*possible_ingredients[allergen])

    ingr_used = set()
    while True:
        cont = False
        for ingr_set in possible_ingredients.values():
            if len(ingr_set) == 1:
                ingr_used.update(ingr_set)
            elif len(ingr_set) > 1:
                cont = True
                ingr_set.difference_update(ingr_used)
        if not cont: break
    
    allergenic = set.union(*possible_ingredients.values())
    print(sum([ingr_count[i] for i in ingr_count if i not in allergenic]))

    t = [(x[0], x[1].pop()) for x in possible_ingredients.items()]
    t.sort()
    print(",".join([x[1] for x in t]))

if __name__ == "__main__":
    main()