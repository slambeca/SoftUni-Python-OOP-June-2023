from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class ISender(ABC):
    def __init__(self, sender):
        self.sender = sender

    @abstractmethod
    def set_sender(self, sender):
        pass


class IReceiver(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def set_receiver(self, receiver):
        pass


class MyMl(IContent):
    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class Sender(ISender):
    def set_sender(self, sender):
        return ''.join(["I'm ", sender, "!"])


class Receiver(IReceiver):
    def set_receiver(self, receiver):
        return ''.join(["I'm ", receiver])


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender, "!"])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver, "!"])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


myml = MyMl("Hello, sir!")
email = Email('IM')
email.set_sender('Robocop')
email.set_receiver('Terminator')
email.set_content(myml)
print(email)

