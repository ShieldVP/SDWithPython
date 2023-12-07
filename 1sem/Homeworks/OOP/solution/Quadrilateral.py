from typing import Tuple

import pandas as pd
import matplotlib.pyplot as plt

from Figure import Figure


def calculate_distance(point_0: Tuple[int, int], point_1: Tuple[int, int]) -> float:
    return ((point_0[0] - point_1[0]) ** 2 + (point_0[1] - point_1[1]) ** 2) ** 0.5


class Quadrilateral(Figure):
    def __str__(self) -> str:
        return 'quadrilateral'

    def calculatePerimeter(self) -> float:
        point_0, point_1, point_2, point_3 = self.points
        perimeter = calculate_distance(point_0, point_1)
        perimeter += calculate_distance(point_1, point_2)
        perimeter += calculate_distance(point_2, point_3)
        perimeter += calculate_distance(point_0, point_3)
        return perimeter

    def calculateSquare(self) -> float:
        point_0, point_1, point_2, point_3 = self.points
        S = point_0[0] * (point_1[1] - point_3[1])
        S += point_1[0] * (point_2[1] - point_0[1])
        S += point_2[0] * (point_3[1] - point_1[1])
        S += point_3[0] * (point_0[1] - point_2[1])
        return abs(S) / 2

    @classmethod
    def constructFromSeries(cls, series: pd.Series) -> object:
        """construct instance from pandas.Series"""
        point_0 = tuple(map(float, series.iloc[1].split(':')))
        point_1 = tuple(map(float, series.iloc[2].split(':')))
        point_2 = tuple(map(float, series.iloc[3].split(':')))
        point_3 = tuple(map(float, series.iloc[4].split(':')))
        return cls(points=(point_0, point_1, point_2, point_3))

    def graphFigure(self):
        """Draw figure via matplotlib.pyplot"""
        coords = list(self.points)
        coords.append(self.points[0])  # make it cyclic
        xs, ys = zip(*coords)

        plt.figure()
        plt.plot(xs, ys)
        plt.show()
