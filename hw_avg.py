"""Решения задач.

Курс 'Методы обработки экспериментальных данных в физике частиц'.
"""
import numpy as np
from ROOT import TRandom3
from scipy.optimize import minimize

from mixins import BasicGraphErrors


class Task1(BasicGraphErrors):
    """Решение задачи 1."""

    STDX, STDY = 0.2, 0.2

    def _likelihood_function(self, params):
        """Логарифм функции правдоподобия. С точностью до константы."""
        p1, p0, *points = params
        residuals_x = self.points[:, 0] - np.array(points)
        residuals_y = self.points[:, 1] - p1 * np.array(points) - p0
        neglog_likelihoods = (
            (residuals_x / self.STDX) ** 2 + (residuals_y / self.STDY) ** 2
        )
        return np.sum(neglog_likelihoods)

    def _likelihood_function_without_x_errors(self, params):
        """Логарифм функции правдоподобия. С точностью до константы."""
        p1, p0 = params
        residuals = self.points[:, 1] - p1 * self.points[:, 0] - p0
        neglog_likelihoods = (
            (residuals / self.STDX) ** 2
        )
        return np.sum(neglog_likelihoods)

    def solution_by_scipy(self):
        """Решение.

        1. Определяем функцию правдоподобия
        2. Осуществляем поиск максимума функции правдоподобия
        """
        initial_guess = [0] * 5
        result = minimize(self._likelihood_function, initial_guess)
        p1, p0, *x_arr = result.x

        self.function.SetParameters(p1, p0)

        self.function_text.AddText('Maximum likelihood method')
        self.function_text.AddText('BLUE: scipy')
        self.function_text.AddText(f'p0:   {round(p0, 2)}')
        self.function_text.AddText(f'p1:   {round(p1, 2)}')
        for i in range(3):
            self.function_text.AddText(f'x{i}:   {round(x_arr[i], 2)}')

    def solution_by_scipy_without_x_errors(self):
        """Тест ММП без ошибок по X."""
        initial_guess = [0] * 2
        result = minimize(
            self._likelihood_function_without_x_errors,
            initial_guess
        )
        p1, p0 = result.x

        self.test_function.SetParameters(p1, p0)

        self.test_function_text.AddText('Maximum likelihood method')
        self.test_function_text.AddText('       without X errors')
        self.test_function_text.AddText('GRAY: scipy')
        self.test_function_text.AddText(f'p0:   {round(p0, 2)}')
        self.test_function_text.AddText(f'p1:   {round(p1, 2)}')

    def solution_by_root(self):
        """Фитирование МНК для сравнения."""
        self.graph.Fit('pol1')
        params = (
            round(self.graph.GetFunction('pol1').GetChisquare(), 2),
            round(self.graph.GetFunction('pol1').GetParameter(0), 2),
            round(self.graph.GetFunction('pol1').GetParameter(1), 2),
            round(self.graph.GetFunction('pol1').GetParError(0), 2),
            round(self.graph.GetFunction('pol1').GetParError(1), 2)
        )

        self.graph_text.AddText('Default is chi-square method')
        self.graph_text.AddText('RED: Fit(pol1)')
        self.graph_text.AddText(f'Chi^2/n:   {params[0]} / 3')
        self.graph_text.AddText(f'p0:        {params[1]} +/- {params[3]}')
        self.graph_text.AddText(f'p1:        {params[2]} +/- {params[4]}')

    def __call__(self):
        """Вызов решений."""
        self.solution_by_root()
        self.solution_by_scipy()
        self.solution_by_scipy_without_x_errors()


if __name__ == '__main__':
    ex, ey = TRandom3(seed=42).Gaus, TRandom3(seed=4242).Gaus
    errors = [
        [abs(ex(0, Task1.STDX)), abs(ey(0, Task1.STDY))]
        for _ in range(3)
    ]
    points_data = [
        [[1, 11], [3, 11.8], [6, 14]],
        [[15, 28], [19, 32.5], [23, 36]],
    ]

    for num, points in enumerate(points_data, start=1):
        Task1(num, points, errors)
