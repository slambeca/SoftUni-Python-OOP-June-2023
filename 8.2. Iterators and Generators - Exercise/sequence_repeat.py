class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.number - 1:
            raise StopIteration

        self.index += 1

        return self.sequence[self.index % len(self.sequence)]
        # 0 % 3 = 0
        # 1 % 3 = 1 (same as 10 % 3)
        # 2 % 3 = 2 (same as 20 % 3)
        # 3 % 3 = 0
        # 4 % 3 = 1
        # 5 % 3 = 2


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')