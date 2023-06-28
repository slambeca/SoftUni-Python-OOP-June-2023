class Guitar:
    def play(self):
        return "Playing the guitar"


def start_playing(some_object):
    return some_object.play()


guitar = Guitar()
print(start_playing(guitar))