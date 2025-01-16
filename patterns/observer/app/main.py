from src.display.current_conditions import CurrentConditionsDisplay
from src.display.statistics import StatisticsDisplay
from src.display.forecast import ForecastDisplay
from src.weather_data import WeatherData

def main():
    
    weather = WeatherData()

    current = CurrentConditionsDisplay(subject=weather)
    statistics = StatisticsDisplay(subject=weather)
    forecast = ForecastDisplay(subject=weather)
    
    weather.register_observer(observer=current)
    weather.register_observer(observer=statistics)
    weather.register_observer(observer=forecast)

    for _ in range(10):
        weather.measurements_changed()

    current.display()
    statistics.display()
    forecast.display()

    print("\nWOW! This forecast is so wrong! Please stop!")

    weather.remove_observer(observer=forecast)

    for _ in range(10):
        weather.measurements_changed()
    
    current.display()
    statistics.display()
    forecast.display()

if __name__=="__main__":
    main()
