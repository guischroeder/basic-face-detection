from abc import ABC, abstractmethod


class AWSClient(ABC):
    @abstractmethod
    def get_instance(self):
        pass
