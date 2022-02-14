from abc import ABC, abstractmethod


class AbstractWordler(ABC):
    def __init__(self):
        self.reset_wordler()

    @abstractmethod
    def get_first_word(self):
        pass

    @abstractmethod
    def get_next_word(self, score):
        pass

    @abstractmethod
    def reset_wordler(self):
        pass
