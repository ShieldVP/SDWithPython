import pandas as pd
import matplotlib.pyplot as plt

from Rectangle import Rectangle


class Square(Rectangle):
    def __str__(self) -> str:
        return 'square'

    def calculatePerimeter(self) -> float:
        perimeter = 4 * self.points[1]
        return perimeter

    def calculateSquare(self) -> float:
        S = self.points[1] ** 2
        return S

    @classmethod
    def constructFromSeries(cls, series: pd.Series) -> object:
        """construct instance from pandas.Series"""
        point_str = series.iloc[1]
        point = tuple(map(float, point_str.split(':')))
        side = float(series.iloc[2])
        return cls(points=(point, side))

    def graphFigure(self):
        """Draw figure via matplotlib.pyplot"""
        point_0 = self.points[0]
        side = self.points[1]
        point_1 = (point_0[0], point_0[1] + side)
        point_2 = (point_0[0] + side, point_0[1] + side)
        point_3 = (point_0[0] + side, point_0[1])
        coords = [point_0, point_1, point_2, point_3, point_0]
        xs, ys = zip(*coords)

        plt.figure()
        plt.plot(xs, ys)
        plt.show()
