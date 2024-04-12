from abc import ABC, abstractmethod


class BaseConverter(ABC):
    @abstractmethod
    def handle(self):
        ...
