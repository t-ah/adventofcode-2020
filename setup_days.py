from shutil import copyfile
import sys

if len(sys.argv) != 2:
    print("Give day number(s) as parameter.")
else:
    days = sys.argv[1]
    start_day = 0
    end_day = 0
    if "-" in days:
        start_day, end_day = [int(x) for x in days.split("-")]
    else:
        start_day = int(days)
        end_day = start_day
    for day in range(start_day, end_day + 1):
        copyfile("template.py", f"day{day}.py")
        with open(f"day{day}.txt", "w") as f:
            pass