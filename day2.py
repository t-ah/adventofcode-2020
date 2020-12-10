import re

with open("day2.txt", "r") as f:
    text = f.readlines()

pattern = re.compile("([0-9]+)-([0-9]+) (.): (.+)")

count = 0
for line in text:
    start, end, letter, pw = re.search(pattern, line).groups()
    letter_count = pw.count(letter)
    if letter_count >= int(start) and letter_count <= int(end):
        count += 1
print(count)


count = 0
for line in text:
    start, end, letter, pw = re.search(pattern, line).groups()
    if (pw[int(start) - 1] == letter) ^ (pw[int(end) - 1] == letter):
        count += 1
print(count)