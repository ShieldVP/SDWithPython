from abc import ABC, abstractmethod
import pandas as pd

class Figure(ABC):
    def __init__(self, points: tuple[tuple, ...]):
        self.points = points
        self.square = self.calculateSquare()
        self.perimeter = self.calculatePerimeter()
        
    @abstractmethod
    def calculatePerimeter(self) -> float:
        pass

    @abstractmethod
    def calculateSquare(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def constructFromSeries(cls,series: pd.Series) -> object:
        """construct instance from pandas.Series"""

    @abstractmethod
    def graphFigure(self):
        """Draw figure via matplotlib.pyplot"""
        pass


