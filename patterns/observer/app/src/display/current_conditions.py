from src.models.display import DisplayElement
from src.models.observer import Observer
from src.models.subject import Subject

class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, subject: Subject) -> None:
        self.subject = subject
        self.temperature = None
        self.humidity  = None
        self.pressure = None
        super().__init__()
    
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
    
    def display(self) -> None:
        print("Current weather:\nTemperature:{:.2f}°C\nHumidity:{:.2f}%\nPressure:{:.2f} hPa"
            .format(self.temperature, self.humidity, self.pressure)
        )
    