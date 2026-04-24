#counter class
class Counter:
    count = 0   # class variable

    def __init__(self):
        Counter.count += 1


c1 = Counter()
c2 = Counter()

print(Counter.count)