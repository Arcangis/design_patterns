from src.entity.statistics_metrics import StatisticsMetrics
from src.models.display import DisplayElement
from src.models.observer import Observer
from src.models.subject import Subject

class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, subject: Subject) -> None:
        self.subject = subject
        self.temperature = StatisticsMetrics()
        self.humidity  = StatisticsMetrics()
        self.pressure = StatisticsMetrics()
        super().__init__()
    
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self.temperature.update(temperature)
        self.humidity.update(humidity)
        self.pressure.update(pressure)
    
    def display(self) -> None:
        print("""Statistics weather:\n  Temperature:\n    Min:{}°C\n    Max:{}°C\n    Average:{}°C\n  Humidity:\n    Min:{}%\n    Max:{}%\n    Average:{}%\n  Pressure:\n    Min:{}hPa\n    Max:{}hPa\n    Average:{}hPa"""
            .format(self.temperature.min, self.temperature.max, self.temperature.average,
                self.humidity.min, self.humidity.max, self.humidity.average, 
                self.pressure.min, self.pressure.max, self.pressure.average
            )
        )
    