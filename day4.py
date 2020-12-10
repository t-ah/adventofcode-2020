import re

def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return f.read().split("\n\n")

def all_present(p):
    return "byr" in p and "iyr" in p and "eyr" in p and "hgt" in p and "hcl" in p and "ecl" in p and "pid" in p

def is_number_between(s, lower, upper):
    n = int(s)
    if n < lower or n > upper: return False
    return True

ecls = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
def all_valid(p):
    if not is_number_between(p["byr"], 1920, 2002):
        return False
    if not is_number_between(p["iyr"], 2010, 2020):
        return False
    if not is_number_between(p["eyr"], 2020, 2030):
        return False
    hgt = p["hgt"]
    hgt_val = hgt[:-2]
    hgt_unit = hgt[-2:]
    if hgt_unit == "in":
        if not is_number_between(hgt_val, 59, 76):
            return False
    elif hgt_unit == "cm":
        if not is_number_between(hgt_val, 150, 193):
            return False
    else:
        return False
    if re.fullmatch(r"#\w{6}", p["hcl"]) == None:
        return False
    if p["ecl"] not in ecls:
        return False
    if re.fullmatch(r"\d{9}", p["pid"]) == None:
        return False
    return True

def main():
    passport_data = [x.split("\n") for x in read_input()]
    passports = []
    for batch in passport_data:
        passport = {}
        passports.append(passport)
        for line in batch:
            entries = line.split(" ")
            for entry in entries:
                passport[entry[:3]] = entry[4:]

    result1 = 0
    result2 = 0
    for passport in passports:
        if all_present(passport):
            result1 += 1
            if all_valid(passport):
                result2 += 1
    print(f"{result1}\n{result2}")

if __name__ == "__main__":
    main()