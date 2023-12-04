"""Решения задач.

Курс 'Методы обработки экспериментальных данных в физике частиц'.
"""
import numpy as np
from ROOT import TRandom3
from scipy.optimize import minimize

from mixins import BasicGraphErrors


class Task1(BasicGraphErrors):
    """Решение задачи 1."""

    STD = 0.2

    def _likelihood_function(self, params):
        """Отрицательный логарифм функции правдоподобия."""
        p1, p0 = params
        residuals = self.points[:, 1] - p1 * self.points[:, 0] - p0
        likelihoods = (
            -np.log(2 * np.pi) / 2 - np.log(self.STD)
            - ((residuals / self.STD) ** 2) / 2
        )
        return -np.sum(likelihoods)

    def solution_by_scipy(self):
        """Решение №1.

        1. Определяем функцию правдоподобия
        2. Осуществляем поиск максимума функции правдоподобия
        """
        initial_guess = [0, 0]
        result = minimize(self._likelihood_function, initial_guess)
        p1, p0 = result.x

        self.function.SetParameters(p1, p0)

        self.function_text.AddText(f'p0:   {round(p0, 2)}')
        self.function_text.AddText(f'p1:   {round(p1, 2)}')

    def solution_by_root(self):
        """Решение №2.

        Используем фитирование из библиотеки PyROOT.
        """
        self.graph.Fit('pol1', 'L')
        self.graph.GetFunction('pol1').SetLineWidth(3)
        params = (
            round(self.graph.GetFunction('pol1').GetChisquare(), 2),
            round(self.graph.GetFunction('pol1').GetParameter(0), 2),
            round(self.graph.GetFunction('pol1').GetParameter(1), 2),
            round(self.graph.GetFunction('pol1').GetParError(0), 2),
            round(self.graph.GetFunction('pol1').GetParError(1), 2)
        )

        self.graph_text.AddText(f'Chi^2/n: {params[0]} / 3')
        self.graph_text.AddText(f'p0:        {params[1]} +/- {params[3]}')
        self.graph_text.AddText(f'p1:        {params[2]} +/- {params[4]}')

    def __call__(self):
        """Выззов решений."""
        self.solution_by_scipy()
        self.solution_by_root()


if __name__ == '__main__':
    ex, ey = TRandom3(seed=42).Gaus, TRandom3(seed=4242).Gaus
    errors = [[abs(ex(0, Task1.STD)), abs(ey(0, Task1.STD))] for _ in range(3)]
    points_data = [
        [[1, 8], [3, 11.1], [6, 14.9]],
        [[15, 28], [19, 31.5], [23, 36]],
        [[1, 11], [3, 11.9], [6, 14]],
    ]

    for num, points in enumerate(points_data, start=1):
        Task1(num, points, errors)
