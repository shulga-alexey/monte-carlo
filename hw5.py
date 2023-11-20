from basic import Basic
from math import factorial, exp
from random import random


class Task1(Basic):
    """Задание 1."""

    def __init__(self, g, M, m):
        """Конструктор."""
        self.nums = [m / M for m in self.__gen_m(g, M, m)]

    @staticmethod
    def __gen_m(g, M, m):
        """Генератор m."""
        for _ in range(Task1.ENTRIES):
            m = (g * m) % M
            yield m


class Task3(Basic):
    """Задание 3."""

    def __init__(self, n, p):
        """Конструктор."""
        self.nums = [0] * super().ENTRIES

        for i in range(super().ENTRIES):
            m = 0
            r = random()
            psi = self.__p_bi_neg(m, n, p)

            while r > 0:
                m += 1.
                r = r - psi
                psi = psi * (m + n - 1.) / m * (1. - p)

            self.nums[i] = m - 1.

    @staticmethod
    def __p_bi_neg(m, n, p):
        """Биномиальное отрицательное распределение."""
        return (
            factorial(m + n - 1) * (p ** n) * ((1 - p) ** m)
            / (factorial(m) * factorial(n - 1))
        )


class Task4(Basic):
    """Задание 4."""

    def __init__(self, n, p):
        """Конструктор."""
        self.nums = [0] * super().ENTRIES

        for i in range(super().ENTRIES):
            m = 0
            r = random()
            psi = self.__poisson(m, n, p)
            while r > 0:
                m += 1
                r = r - psi
                psi = psi * n / m

            self.nums[i] = m - 1.

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

    def __init__(self):
        """Конструктор."""
        pass


if __name__ == '__main__':
    A = 13, 17, 3
    B = 5 ** 17, 2 ** 42, 1
    Task1(*A).hist('Task 1(A)')
    Task1(*B).hist('Task 1(B)')

    Task3(10, 0.1).hist()
    Task4(5, 0.1).hist()
