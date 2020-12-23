class RingBuffer:
    def __init__(self, content, extension):
        self.lookup = {}
        elements = [RBElement(int(c) - 1) for c in content]
        for i in range(len(elements), extension):
            elements.append(RBElement(i))

        self.n = len(elements)
        for i in range(len(elements)):
            elements[i].next = elements[(i+1) % len(elements)]
            self.lookup[elements[i].value] = elements[i]
        elements[-1].next = elements[0]
        self.current = elements[0]

    def step(self):
        picked_up = [self.current.next]
        for _ in range(2):
            picked_up.append(picked_up[-1].next)
        self.current.next = picked_up[-1].next
        picked_up_values = [e.value for e in picked_up]
        destination = (self.current.value - 1) % self.n
        while destination in picked_up_values:
            destination = (destination - 1) % self.n
        destination_element = self.lookup[destination]
        picked_up[-1].next = destination_element.next
        destination_element.next = picked_up[0]
        self.current = self.current.next

    def current_order(self):
        element = self.current
        result = []
        for _ in range(self.n):
            result.append(element.value + 1)
            element = element.next
        return result

    def result_for2(self):
        one_element = self.lookup[0]
        return (one_element.next.value + 1) * (one_element.next.next.value + 1)

class RBElement:
    def __init__(self, value):
        self.value = value
        self.next = None

def main():
    labeling = "853192647"
    b = RingBuffer(labeling, 0)
    for _ in range(100):
        b.step()
    order = "".join([str(x) for x in b.current_order()])
    order = order.split("1")
    print(order[1] + order[0])

    b = RingBuffer(labeling, 1000000)
    for _ in range(10000000):
        b.step()
    print(b.result_for2())

if __name__ == "__main__":
    main()