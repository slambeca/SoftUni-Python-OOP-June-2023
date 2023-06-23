from project.animal import Animal


class Dog(Animal):
    def bark(self):
        return "barking..."

# Variant 2
# from project.animal import Animal


# class Dog(Animal):
#     @staticmethod
#     def bark():
#         return "barking..."
