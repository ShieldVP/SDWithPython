import pandas as pd
import matplotlib.pyplot as plt

from Quadrilateral import Quadrilateral


class Rectangle(Quadrilateral):
    def __str__(self) -> str:
        return 'rectangle'

    def calculatePerimeter(self) -> float:
        point_0, point_1 = self.points
        first_side = point_1[0] - point_0[0]
        second_side = point_1[1] - point_0[1]
        perimeter = 2 * (first_side + second_side)
        return perimeter

    def calculateSquare(self) -> float:
        point_0, point_1 = self.points
        first_side = point_1[0] - point_0[0]
        second_side = point_1[1] - point_0[1]
        S = first_side * second_side
        return S

    @classmethod
    def constructFromSeries(cls, series: pd.Series) -> object:
        """construct instance from pandas.Series"""
        point_0 = tuple(map(float, series.iloc[1].split(':')))
        point_1 = tuple(map(float, series.iloc[2].split(':')))
        return cls(points=(point_0, point_1))

    def graphFigure(self):
        """Draw figure via matplotlib.pyplot"""
        point_0, point_2 = self.points
        point_1 = (point_0[0], point_2[1])
        point_3 = (point_2[0], point_0[1])
        coords = [point_0, point_1, point_2, point_3, point_0]
        xs, ys = zip(*coords)

        plt.figure()
        plt.plot(xs, ys)
        plt.show()
