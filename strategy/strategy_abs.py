from abc import ABC
from abc import abstractmethod


class MessageOutput(ABC):
    @abstractmethod
    def send_msg(self) -> None:
        pass
