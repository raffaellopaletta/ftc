from abc import ABC, abstractmethod


class AbstractTokenizer(ABC):

    @abstractmethod
    def tokenize(self, text: str):
        pass


