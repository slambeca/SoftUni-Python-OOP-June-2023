class dictionary_iter:
    def __init__(self, kwargs):
        self.kwargs = list(kwargs.items())[::-1]
        self.iterations = 0
        self.len_kwargs = len(self.kwargs)

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.len_kwargs:
            raise StopIteration

        self.iterations += 1

        return self.kwargs.pop()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
