from abc import ABC, abstractmethod


class AbstractWordler(ABC):
    @abstractmethod
    def get_first_word(self):
        pass

    @abstractmethod
    def get_next_word(self, score):
        pass

    @abstractmethod
    def reset_wordler(self):
        pass
