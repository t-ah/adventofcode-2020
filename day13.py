import sys, math

def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return f.read().split("\n")

def chinese_remainder(n, a):
    sum = 0
    prod = math.prod(n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * pow(p, -1, n_i) * p
    return sum % prod

def main():
    lines = read_input()
    time = int(lines[0])
    bus_times = lines[1].split(",")

    shortest_wait = sys.maxsize
    result = -1
    for bt in bus_times:
        if bt == "x":
            continue
        bus_time = int(bt)
        wait_time = bus_time - (time % bus_time)
        if wait_time < shortest_wait:
            shortest_wait = wait_time
            result = bus_time * wait_time
    print(result)

    factors = []
    for i in range(len(bus_times)):
        if bus_times[i] != "x":
            factors.append([i, int(bus_times[i])])
    max_i = factors[-1][0]
    for f in factors:
        f[0] = max_i - f[0]

    a = [x[0] for x in factors]
    n = [x[1] for x in factors]
    print(chinese_remainder(n,a) - factors[0][0])

if __name__ == "__main__":
    main()