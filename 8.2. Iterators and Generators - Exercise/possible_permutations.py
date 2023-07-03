from itertools import permutations


def possible_permutations(numbers):
    for element in permutations(numbers):
        yield list(element)


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]