"""Решения задач домашнего задания №5."""
from math import exp, factorial
from random import random

from mixins import Basic


class Task1(Basic):
    """Задание 1."""

    def __init__(self, g, M, m, *args):
        """Конструктор."""
        super().__init__(*args)

        num = 0
        for _ in range(super().ENTRIES):
            m = (g * m) % M
            num = m / M
            self.histogram.Fill(num)

        super()._get_histogram()


class Task3(Basic):
    """Задание 3."""

    def __init__(self, n, p, *args):
        """Конструктор."""
        super().__init__(*args)

        for _ in range(super().ENTRIES):
            m = 0
            r = random()
            psi = self.__pascal(m, n, p)

            while r > 0:
                m += 1.
                r = r - psi
                psi = psi * (m + n - 1.) / m * (1. - p)

            self.histogram.Fill(m - 1.)

        super()._get_histogram()

    @staticmethod
    def __pascal(m, n, p):
        """Биномиальное отрицательное распределение."""
        return (
            factorial(m + n - 1) * (p ** n) * ((1 - p) ** m)
            / (factorial(m) * factorial(n - 1))
        )


class Task4(Basic):
    """Задание 4."""

    def __init__(self, n, p, *args):
        """Конструктор."""
        super().__init__(*args)

        for _ in range(super().ENTRIES):
            m = 0
            r = random()
            psi = self.__poisson(m, n, p)

            while r > 0:
                m += 1
                r = r - psi
                psi = psi * n / m

            self.histogram.Fill(m - 1.)

        super()._get_histogram()

    @staticmethod
    def __poisson(m, n, p):
        """Распределение Пуассона."""
        return (n ** m) / factorial(m) * exp(-n)


class Task5(Basic):
    """Задание 5."""

    def __init__(self):
        """Конструктор."""
        pass


class Task7(Basic):
    """Задание 7."""

    def __init__(self):
        """Конструктор."""
        pass


class Task8(Basic):
    """Задание 8."""

    def __init__(self, lmbd, *args):
        """Конструктор."""
        super().__init__(*args)

        for _ in range(super().ENTRIES):
            m = 0
            q = random()

            while q >= exp(-lmbd):
                m += 1
                q *= random()

            self.histogram.Fill(m)

        super()._get_histogram()
