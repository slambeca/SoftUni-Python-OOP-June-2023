from abc import ABC, abstractmethod


class Cable(ABC):
    @abstractmethod
    def connect(self, d1, d2):
        pass


class HDMICable(Cable):
    def connect(self, device1, device2):
        return f"Connect {device1} to {device2} via HDMI"


class RCACable(Cable):
    def connect(self, device1, device2):
        return f"Connect {device1} to {device2} via RCACable"


class EthernetCable(Cable):
    def connect(self, device1, device2):
        return f"Connect {device1} to {device2} via Ethernet"


class PowerOutlet(Cable):
    def connect(self, destination, _):
        return f"Connect device to power"


class DVDPlayer:
    pass


class GameConsole:
    pass


class Router:
    pass


class Television:
    pass


hdmi = HDMICable()
tv = Television()
gc = GameConsole()


print(hdmi.connect(tv, gc))
# Connect <__main__.Television object at 0x00000072C9FEB310> to <__main__.GameConsole object at 0x00000072C9FEB2E0>
# via HDMI