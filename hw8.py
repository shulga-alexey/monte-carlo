"""Решения задач домашнего задания №8."""
import math

import ROOT

from mixins import BasicHist

BasicHist.HW_NUM = 8


class Task1(BasicHist):
    """Задача 1."""

    def __call__(self):
        """Решение."""
        rndm1, rndm2 = ROOT.TRandom3(seed=42).Rndm, ROOT.TRandom3(seed=84).Rndm

        for _ in range(super().ENTRIES):
            g1, g2 = rndm1(), rndm2()

            if g1 <= 5/6:
                num = 2 * g2
            elif 2 * g2 - 1 >= 0:
                num = 1 + (2 * g2 - 1) ** (1/5)
            else:
                num = 1 - (1 - 2 * g2) ** (1/5)

            self.histogram.Fill(num)


class Task2(BasicHist):
    """Задача 2."""

    def __call__(self):
        """Решение."""
        pass
