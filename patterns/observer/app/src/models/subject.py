from abc import ABC

from src.models.observer import Observer

class Subject(ABC):

    def __init__(self):
        self._observer_list = []

    def register_observer(self, observer: Observer):
        self._observer_list.append(observer)

    def remove_observer(self, observer: Observer):
        self._observer_list.remove(observer)

    def notify_observers(self, temperature: float, humidity: float, pressure: float) -> None:
        for observer in self._observer_list:
            observer.update(temperature, humidity, pressure)
