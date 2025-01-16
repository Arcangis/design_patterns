from random import uniform

from src.models.subject import Subject

class WeatherData(Subject):
    
    def __init__(self):
        self._observer_list = []
        super().__init__()
    
    def get_temperature(self) -> float:
        return uniform(20, 35)

    def get_humidity(self) -> float:
        return uniform(70, 100)
    
    def get_pressure(self) -> float:
        return uniform(1010, 1015)
    
    def measurements_changed(self) -> None:
        self.notify_observers(
            temperature=self.get_temperature(),
            humidity=self.get_humidity(),
            pressure=self.get_pressure()
        )
    