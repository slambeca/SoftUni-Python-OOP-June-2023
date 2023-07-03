def number_increment(numbers):
    def increase():
        new_numbers = []
        for num in numbers:

            new_numbers.append(num + 1)

        return new_numbers

    return increase()    # If we don`t have () here, we have to use them below, in the outside function call


print(number_increment([1, 2, 3]))

# Variant 2
# def number_increment(numbers):
#     def increase():
#         new_numbers = []
#         for num in numbers:
#             new_numbers.append(num + 1)

#         return new_numbers

#     return increase


# print(number_increment([1, 2, 3])())

# Variant 3
# def number_increment(numbers):
#     def increase():
#         return [x + 1 for x in numbers]
# 
#     return increase()
# 
# 
# print(number_increment([1, 2, 3]))
