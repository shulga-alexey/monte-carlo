"""Решения задач.

Курс 'Методы обработки экспериментальных данных в физике частиц'.
"""

from array import array
from time import sleep

import numpy as np
from ROOT import TCanvas, TGraphErrors, TF1
from scipy.optimize import minimize


class BasicGraphErrors:
    """Базовый класс для отрисовки графика."""

    def __init__(self, points, errors):
        """Конструктор."""
        self.points = np.array(points)
        self.errors = np.array(errors)

        self.canvas = TCanvas('c1', 'Graph', 200, 10, 700, 500)
        self.canvas.SetGrid()
        self.canvas.GetFrame().SetFillColor(21)
        self.canvas.GetFrame().SetBorderSize(12)

        
        self.function = TF1('fun1', '[0]*x+[1]')

        self.graph = TGraphErrors(
            3,
            array('f', self.points[:, 0]),
            array('f', self.points[:, 1]),
            array('f', self.errors[:, 0]),
            array('f', self.errors[:, 1])
        )
        self.graph.SetTitle('TGraphErrors Example')
        self.graph.SetMarkerColor(4)
        self.graph.SetMarkerStyle(21)

        #self()

        self.function.SetParameters(1, 1)
        self.graph.Draw('AP')
        self.function.Draw('same')
        self.canvas.Update()
        self.canvas.Draw()
        sleep(4)


class Task1(BasicGraphErrors):
    """Решение задачи 1."""

    def _likelihood_function(self, params):
        """Функция правдоподобия."""
        a, b = params
        residuals = self.points[:, 1] - a * self.points[:, 0] + b
        likelihoods = (
            1 / (np.sqrt(2 * np.pi) * self.errors[:, 1]) *
            np.exp(-0.5 * ((residuals / self.errors[:, 1]) ** 2))
        )

        return -np.sum(np.log(likelihoods))

    def solution_by_hand(self):
        """Решение №1.

        1. Определяем функцию правдоподобия _likelihood_function
        2. Осуществляем поиск максимума функции правдоподобия
        """
        initial_guess = [0, 0]
        result = minimize(self._likelihood_function, initial_guess)
        a, b = result.x

        print(
            f' Для прямой y = a * x + b имеем:\n'
            f' a = {round(a, 2)} +-\n'
            f' b = {round(b, 2)} +-\n'
        )
        self.function.SetParameters(a, b)

    def solution_by_clear_root(self):
        """Решение №2.

        Используем фитирование из библиотеки PyROOT.
        """
        #self.graph.Fit('pol1', 'L')

    def __call__(self):
        """Поиск максимума функции правдоподобия."""
        self.solution_by_hand()
        self.solution_by_clear_root()


if __name__ == '__main__':
    Task1([[1,4],[3,6],[5,10]], [[0.1,0.15],[0.2,0.25],[0.3,0.35]])
