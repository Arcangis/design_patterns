from random import uniform

from src.models.display import DisplayElement
from src.models.observer import Observer
from src.models.subject import Subject

class ForecastDisplay(Observer, DisplayElement):

    def __init__(self, subject: Subject) -> None:
        self.subject = subject
        self.temperature = None
        self.humidity  = None
        self.pressure = None
        super().__init__()
    
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self.temperature = temperature + uniform(-10, 10)
        self.humidity = humidity + uniform(-5, 5)
        self.pressure = pressure + uniform(-0.5, 0.5)
    
    def display(self) -> None:
        print("Forecast weather:\nTemperature:{:.2f}°C\nHumidity:{:.2f}%\nPressure:{:.2f} hPa"
            .format(self.temperature, self.humidity, self.pressure)
        )
    