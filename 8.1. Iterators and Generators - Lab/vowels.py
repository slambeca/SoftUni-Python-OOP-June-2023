class vowels:
    VOWELS = ["a", "e", "i", "u", "o", "y"]

    def __init__(self, text):
        self.text = [x for x in text[::-1] if x.lower() in self.VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.text:
            raise StopIteration

        return self.text.pop()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)