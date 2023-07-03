def genrange(start, end):
    num = start

    while num <= end:
        yield num

        num += 1


print(list(genrange(1, 10)))


# Variant 2


# def genrange(start, end):
#     for num in range(start, end + 1):
#         yield num
# 
# 
# print(list(genrange(1, 10)))
