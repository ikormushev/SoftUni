from abc import ABC, abstractmethod


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


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def content_type(self):
        pass


class IProtocol(ABC):
    @abstractmethod
    def protocol_type(self, name):
        pass


class IMProtocol(IProtocol):
    def protocol_type(self, name):
        return ''.join(["I'm ", name])


class MyMl(IContent):
    def content_type(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class Email(IEmail):
    def __init__(self, protocol: IProtocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    @property
    def protocol(self):
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol: IProtocol):
        self.__protocol = protocol

    def set_sender(self, name):
        self.__sender = self.protocol.protocol_type(name)

    def set_receiver(self, name):
        self.__receiver = self.protocol.protocol_type(name)

    def set_content(self, content: IContent):
        self.__content = content.content_type()

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"
