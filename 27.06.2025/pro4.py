class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        for i in range(self.start, 0, -1):
            yield i

for i in Countdown(5):
    print(i)
