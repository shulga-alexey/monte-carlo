"""Решения задач домашнего задания №5."""
from math import exp, factorial, modf, sqrt
from random import gauss, random

from mixins import BasicHist

BasicHist.HW_NUM = 5


class Task1(BasicHist):
    """Задание 1."""

    def __call__(self, g, M, m):
        """Решение."""
        for _ in range(super().ENTRIES):
            m = (g * m) % M
            num = m / M
            self.histogram.Fill(num)


class Task2(BasicHist):
    """Задание 2."""

    def __call__(self, n, p):
        """Решение."""
        nums = [self.__binomial(i, n, p) for i in range(n)]

        for _ in range(super().ENTRIES):
            r = random()

            for i in range(n):
                sum_lower, sum_upper = sum(nums[:i]), sum(nums[:i + 1])

                if sum_lower <= r <= sum_upper:
                    self.histogram.Fill(i)
                    break

    @staticmethod
    def __binomial(m, n, p):
        """Биномиальное распределение."""
        return (
            factorial(n) * (p ** m) * ((1 - p) ** (n - m))
            / (factorial(m) * factorial(n - m))
        )


class Task3(BasicHist):
    """Задание 3."""

    def __call__(self, n, p):
        """Решение."""
        for _ in range(super().ENTRIES):
            m = 0
            r = random()
            psi = self.__pascal(m, n, p)

            while r > 0:
                m += 1.
                r = r - psi
                psi = psi * (m + n - 1.) / m * (1. - p)

            self.histogram.Fill(m - 1.)

    @staticmethod
    def __pascal(m, n, p):
        """Биномиальное отрицательное распределение."""
        return (
            factorial(m + n - 1) * (p ** n) * ((1 - p) ** m)
            / (factorial(m) * factorial(n - 1))
        )


class Task4(BasicHist):
    """Задание 4."""

    def __call__(self, n, p):
        """Решение."""
        for _ in range(super().ENTRIES):
            m = 0
            r = random()
            psi = self.__poisson(m, n, p)

            while r > 0:
                m += 1
                r = r - psi
                psi = psi * n / m

            self.histogram.Fill(m - 1.)

    @staticmethod
    def __poisson(m, n, p):
        """Распределение Пуассона."""
        return (n ** m) / factorial(m) * exp(-n)


class Task5(BasicHist):
    """Задание 5."""

    def __call__(self, M, intpart=True):
        """Решение."""
        r_func = (
            (lambda x: modf(x * M)[1]) if intpart else
            (lambda x: modf(x * M)[0])
        )

        cov = 0
        for _ in range(M):
            q = random()
            r = r_func(q)
            cov += (q - 0.5) * (r - 0.5)
            self.histogram.Fill(r)

        print(f'cor = {cov * 12 / M}')


class Task7(BasicHist):
    """Задание 7."""

    def __call__(self, n, p):
        """Решение."""
        for _ in range(super().ENTRIES):
            q = gauss(mu=0., sigma=1.)
            _, intpart = modf(n * p + q * sqrt(n * p * (1 - p)))
            self.histogram.Fill(intpart)


class Task8(BasicHist):
    """Задание 8."""

    def __call__(self, lmbd):
        """Решение."""
        for _ in range(super().ENTRIES):
            m = 0
            q = random()

            while q >= exp(-lmbd):
                m += 1
                q *= random()

            self.histogram.Fill(m)
