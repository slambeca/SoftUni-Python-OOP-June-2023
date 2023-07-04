def vowel_filter(func_ref):
    vowels = ["a", "e", "o", "i", "e", "y"]

    def wrapper():
        result = func_ref()
        return [x for x in result if x.lower() in vowels]

    return wrapper


@vowel_filter    # Decorators are functions that change the behavior of a function
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
