"""Решения задач.

Курс 'Методы обработки экспериментальных данных в физике частиц'.
"""

from array import array
from time import sleep

import numpy as np
from ROOT import TF1, TCanvas, TGraphErrors, TPaveText
from scipy.optimize import minimize


class BasicGraphErrors:
    """Базовый класс для отрисовки графика."""

    def __init__(self, name, points, errors):
        """Конструктор."""
        self.points = np.array(points)
        self.errors = np.array(errors)

        self.canvas = TCanvas('c1', 'Graph', 200, 10, 700, 500)
        self.canvas.SetGrid()
        self.canvas.SetBorderSize(12)
        self.canvas.SetFillColor(42)

        self.graph = TGraphErrors(
            3,
            array('f', self.points[:, 0]),
            array('f', self.points[:, 1]),
            array('f', self.errors[:, 0]),
            array('f', self.errors[:, 1])
        )
        self.graph.SetTitle('Linear graph: Y(X) = p1*X + p0')
        self.graph.SetLineColor(2)
        self.graph.SetLineWidth(2)
        self.graph.SetMarkerColor(2)
        self.graph.SetMarkerStyle(21)
        self.graph.GetXaxis().SetTitle('X title')
        self.graph.GetYaxis().SetTitle('Y title')

        self.graph_text = TPaveText(0.67, 0.6, 0.87, 0.45, "NDC")

        self.function = TF1('fun1', '[0]*x+[1]', 0, 100)
        self.function.SetLineColor(4)
        self.function.SetLineWidth(2)

        self.function_text = TPaveText(0.15, 0.6, 0.28, 0.5, "NDC")

        self()

        self.graph.Draw('AP')
        self.graph_text.Draw('same')
        self.function.Draw('same')
        self.function_text.Draw('same')

        self.canvas.Update()
        self.canvas.GetFrame().SetFillColor(0)
        self.canvas.GetFrame().SetBorderSize(12)
        self.canvas.Modified()
        self.canvas.Update()
        self.canvas.Print(f'./img/hw_awg/Task1_{name}.png')

        sleep(5)


class Task1(BasicGraphErrors):
    """Решение задачи 1."""

    def _likelihood_function(self, params):
        """Отрицательный логарифм функции правдоподобия."""
        a, b = params
        residuals = self.points[:, 1] - a * self.points[:, 0] - b
        likelihoods = (
            -np.log(2 * np.pi) / 2 - np.log(self.errors[:, 1]) -
            ((residuals / self.errors[:, 1]) ** 2) / 2
        )
        # Возвращаем отрицательный логарифм функции правдоподобия
        # (так как minimize ищет минимум)
        return -np.sum(likelihoods)

    def solution_by_scipy(self):
        """Решение №1.

        1. Определяем функцию правдоподобия _likelihood_function
        2. Осуществляем поиск максимума функции правдоподобия
        """
        initial_guess = [0, 0]
        result = minimize(self._likelihood_function, initial_guess)
        p1, p0 = result.x

        self.function.SetParameters(p1, p0)

        self.function_text.SetTextAlign(12)
        self.function_text.SetFillColor(43)
        self.function_text.AddText('BLUE: scipy')
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

        self.graph_text.SetTextAlign(12)
        self.graph_text.SetFillColor(43)
        self.graph_text.AddText(' RED: Fit(pol1, L)')
        self.graph_text.AddText(f'Chi^2/ndf: {params[0]} / 3')
        self.graph_text.AddText(f'p0:        {params[1]} +/- {params[3]}')
        self.graph_text.AddText(f'p1:        {params[2]} +/- {params[4]}')

    def __call__(self):
        """Выззов решений."""
        self.solution_by_scipy()
        self.solution_by_root()


if __name__ == '__main__':
    Task1(
        1,
        [[15, 18], [19, 21], [23, 26]],
        [[0.1, 0.15], [0.2, 0.25], [0.3, 0.35]]
    )
    Task1(
        2,
        [[1, 0], [3, 2], [6, 3]],
        [[0.19, 0.15], [0.21, 0.2], [0.33, 0.35]]
    )
    Task1(
        3,
        [[1, -2], [3, 2], [6, 5]],
        [[0.19, 0.15], [0.21, 0.21], [0.33, 0.35]]
    )
