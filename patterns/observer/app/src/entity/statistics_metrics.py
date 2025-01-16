class StatisticsMetrics:
    
    def __init__(self):
        self._min = None
        self._max = None
        self._average = None

    @property
    def min(self) -> float:
        return "{:.2f}".format(self._min)
        
    @property
    def max(self) -> float:
        return "{:.2f}".format(self._max)
    
    @property
    def average(self) -> float:
        return "{:.2f}".format(self._average)
    
    def update(self, value: float):
        if self._min is None or value < self._min:
            self._min = value

        if self._max is None or value > self._max:
            self._max = value

        if self._min is not None and self._max is not None:
            self._average = (self._min + self._max) / 2
    