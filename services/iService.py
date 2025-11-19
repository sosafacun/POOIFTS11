from abc import ABC, abstractmethod
from utils.rich_ui import RichUI as ui

#Interface for all the services. The names explain what each method will do.
class IService(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def search(self):
        pass
        