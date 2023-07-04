def vowel_filter(func_ref):
    vowels = ["a", "e", "o", "i", "e", "y"]

    def wrapper():
        result = func_ref()
        return [x for x in result if x in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())