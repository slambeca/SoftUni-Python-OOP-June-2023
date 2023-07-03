def reverse_text(string):
    for letter in string[::-1]:
        yield letter


for char in reverse_text("step"):
    print(char, end='')

# Variant 2
# def reverse_text(string):
#     yield string[::-1]


# for char in reverse_text("step"):
#     print(char, end='')
