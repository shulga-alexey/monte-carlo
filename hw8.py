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

    def __call__(self, c1):
        """Решение."""
        r1, r2, r3 = (ROOT.TRandom3(seed=(42 * i)).Rndm for i in range(1, 4))
        g = 0.98

        for _ in range(super().ENTRIES):
            g1, g2, g3 = r1(), r2(), r3()

            if g1 <= c1 and g2 <= 0.75:
                num = 2 * g3 - 1
            elif g1 <= c1 and g2 > 0.75 and 2 * g3 - 1 >= 0:
                num = (2 * g3 - 1) ** (1/3)
            elif g1 <= c1 and g2 > 0.75 and 2 * g3 - 1 < 0:
                num = -(1 - 2 * g3) ** (1/3)
            else:
                num = (1 + g ** 2 -
                       ((1 - g ** 2) / (1 - g + 2 * g * g3)) ** 2) / (2 * g)

            self.histogram.Fill(num)
