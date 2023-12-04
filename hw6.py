"""Решения задач домашнего задания №6."""
import ROOT
import math

from mixins import BasicHist

BasicHist.HW_NUM = 6


class Task1(BasicHist):
    """Задача 1."""

    def __call__(self):
        """Решение."""
        pass


class Task3(BasicHist):
    """Задача 3."""

    def __call__(self, g):
        """Решение."""
        random = ROOT.TRandom3(seed=42).Rndm

        for _ in range(super().ENTRIES):
            num = (
                2 * random() - 1 if g == 0 else
                (1 + g ** 2 - ((1 - g ** 2)
                               / (1 - g + 2 * g * random())) ** 2) / (2 * g)
            )
            self.histogram.Fill(num)


class Task5(BasicHist):
    """Задача 5."""

    def __call__(self, a, b):
        """Решение. f(x) = b*x + a."""
        random = ROOT.TRandom3(seed=42).Rndm

        for _ in range(super().ENTRIES):
            num = (-a + math.sqrt(a ** 2 + 2 * b * random())) / b
            self.histogram.Fill(num)


class Task6(BasicHist):
    """Задача 6."""

    def __call__(self):
        """Решение."""
        random = ROOT.TRandom3(seed=42).Rndm
        p_1 = 2 * math.log(2) / math.log(4 * math.exp(1))

        for _ in range(super().ENTRIES):
            q = random()
            num = (
                math.sqrt(q / p_1) if q <= p_1 else
                (2 - math.log(2 * (1 + math.log(2))
                              - math.log(4 * math.exp(1)) * q) / math.log(2))
            )
            self.histogram.Fill(num)
