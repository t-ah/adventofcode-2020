def read_input():
    with open(__file__.replace("py", "txt"), "r") as f:
        return f.read().split("\n")

class TicketField:
    def __init__(self, line):
        spl = line.split(": ")
        self.name = spl[0]
        
        ranges = spl[1].split(" or ")
        self.ranges = [tuple(map(int, x.split("-"))) for x in ranges]

    def is_valid(self, n):
        for r in self.ranges:
            if n >= r[0] and n <= r[1]:
                return True
        return False

def main():
    # "parse" input
    lines = read_input()
    fields = [TicketField(x) for x in lines[:20]]
    my_ticket = [int(x) for x in lines[22].split(",")]
    other_tickets = lines[25:]

    # part 1
    err_rate = 0
    valid_tickets = []
    for t in other_tickets:
        values = [int(x) for x in t.split(",")]
        ticket_valid = True
        for val in values:
            valid = False
            for field in fields:
                if field.is_valid(val):
                    valid = True
                    break
            if not valid:
                err_rate += val
                ticket_valid = False
        if ticket_valid:
            valid_tickets.append(values)
    print(err_rate)

    # initial list of possible fields per index
    field_names = [f.name for f in fields]
    possible_fields = []
    for _ in range(len(fields)):
        possible_fields.append(set(field_names))

    # eliminate by ranges
    for values in valid_tickets:
        for i in range(len(values)):
            val = values[i]
            for field in fields:
                if not field.is_valid(val):
                    possible_fields[i].remove(field.name)
    
    # remove those where another index only has 1 choice left
    while sum([len(x) for x in possible_fields]) > len(fields):
        fixed = [x for s in possible_fields if len(s) == 1 for x in s]
        for s in possible_fields:
            if len(s) > 1:
                for item in fixed:
                    s.discard(item)
    
    # multiply results
    result = 1
    for i in range(len(possible_fields)):
        name = possible_fields[i].pop()
        if name.startswith("departure"):
            result *= my_ticket[i]
    print(result)

if __name__ == "__main__":
    main()