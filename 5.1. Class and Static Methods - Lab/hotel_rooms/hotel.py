from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [room for room in self.rooms if room.number == room_number][0]
        return room.take_room(people)

    def free_room(self, room_number):
        room = [room for room in self.rooms if room.number == room_number][0]
        return room.free_room()

    def status(self):
        free_rooms = [r.number for r in self.rooms if not r.is_taken]
        taken_rooms = [r.number for r in self.rooms if r.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(str(x) for x in free_rooms)}\n" \
               f"Taken rooms: {', '.join(str(x) for x in taken_rooms)}"

# Variant 2
# from project.room import Room


# class Hotel:
#     def __init__(self, name):
#         self.name = name
#         self.rooms = []
#         self.guests = 0

#     @classmethod
#     def from_stars(cls, stars_count):
#         return cls(f"{stars_count} stars Hotel")

#     def add_room(self, room: Room):
#         self.rooms.append(room)

#     def take_room(self, room_number, people):
#         room = self.find_room_by_number(room_number)
#         if not room.is_taken and people <= room.capacity:
#             self.guests += people
#             room.is_taken = True
#             room.guests = people

#     def free_room(self, room_number):
#         room = self.find_room_by_number(room_number)
#         if room.is_taken:
#             room.is_taken = False
#             self.guests -= room.guests
#             room.guests = 0

#     def find_room_by_number(self, room_number):
#         for room in self.rooms:
#             if room.number == room_number:
#                 return room

#         return None

#     def status(self):
#         result = f"Hotel {self.name} has {self.guests} total guests\n"
#         free_rooms = [room.number for room in self.rooms if not room.is_taken]
#         taken_rooms = [room.number for room in self.rooms if room.is_taken]
#         result += f"Free rooms: {', '.join(str(x) for x in free_rooms)}\n"
#         result += f"Taken rooms: {', '.join(str(x) for x in taken_rooms)}"

#         return result
