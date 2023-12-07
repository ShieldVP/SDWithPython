import pandas as pd
import matplotlib.pyplot as plt

from Ellipse import Ellipse


class Circle(Ellipse):
    def __str__(self) -> str:
        return 'circle'

    def calculatePerimeter(self) -> float:
        return 2 * self.pi * self.points[1]

    def calculateSquare(self) -> float:
        return self.pi * self.points[1] ** 2

    @classmethod
    def constructFromSeries(cls, series: pd.Series) -> object:
        """construct instance from pandas.Series"""
        point_str = series.iloc[1]
        point = tuple(map(float, point_str.split(':')))
        radius = float(series.iloc[2])
        return cls(points=(point, radius))

    def graphFigure(self):
        """Draw figure via matplotlib.pyplot"""
        circle = plt.Circle(self.points[0], self.points[1], fill=False)
        fig, ax = plt.subplots()
        ax.set_xlim((self.points[0][0] - self.points[1], self.points[0][0] + self.points[1]))
        ax.set_ylim((self.points[0][1] - self.points[1], self.points[0][1] + self.points[1]))
        ax.add_patch(circle)
        fig.show()
