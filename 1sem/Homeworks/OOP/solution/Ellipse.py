import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from Figure import Figure


class Ellipse(Figure):
    pi = 3.1415926

    def __str__(self) -> str:
        return 'ellipse'

    def calculatePerimeter(self) -> float:
        a, b = self.points[1], self.points[2]
        return self.pi * (3 * (a + b) - ((3 * a + b) * (a + 3 * b)) ** 0.5)

    def calculateSquare(self) -> float:
        return self.pi * self.points[1] * self.points[2]

    @classmethod
    def constructFromSeries(cls, series: pd.Series) -> object:
        """construct instance from pandas.Series"""
        point_str = series.iloc[1]
        point = tuple(map(float, point_str.split(':')))
        a = float(series.iloc[2])
        b = float(series.iloc[3])
        return cls(points=(point, a, b))

    def graphFigure(self):
        """Draw figure via matplotlib.pyplot"""
        ellipse = patches.Ellipse(xy=self.points[0], width=self.points[1] * 2, height=self.points[2] * 2, fill=False)
        fig, ax = plt.subplots()
        ax.set_xlim((self.points[0][0] - self.points[1], self.points[0][0] + self.points[1]))
        ax.set_ylim((self.points[0][1] - self.points[2], self.points[0][1] + self.points[2]))
        ax.add_patch(ellipse)
        fig.show()
