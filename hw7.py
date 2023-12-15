"""Решения задач домашнего задания №7."""
import math
import time

import numpy as np
import ROOT

from mixins import BasicGraph, BasicGraph2D, BasicHist

BasicHist.HW_NUM = 7
BasicGraph.HW_NUM = 7
BasicGraph2D.HW_NUM = 7


class Task1(BasicGraph2D):
    """Задача 1."""

    def __call__(self):
        """Решение."""
        r = h = 1
        g1, g2, g3 = (ROOT.TRandom3(seed=(i * 42)).Rndm for i in range(1, 4))
        gen_xyz = (lambda g1, g2, g3: (
            r * math.sqrt(g2) * math.cos(2 * math.pi * g1),
            r * math.sqrt(g2) * math.sin(2 * math.pi * g1),
            h * g3
        ))

        for i in range(super().ENTRIES):
            self.graph.SetPoint(i, *gen_xyz(g1(), g2(), g3()))


class Task2:
    """Задача 2."""

    def __init__(self):
        """Решение."""
        r = 1
        g1, g2, g3, g4 = (
            ROOT.TRandom3(seed=(i * 42)).Rndm for i in range(1, 5)
        )
        coor = (lambda g1, g2: {
            'x': r * math.sqrt(g2) * math.cos(2 * math.pi * g1),
            'y': r * math.sqrt(g2) * math.sin(2 * math.pi * g1)
        })
        dist = (lambda coor1, coor2: math.sqrt(
            (coor1['x'] - coor2['x']) ** 2 + (coor1['y'] - coor2['y']) ** 2
        ))

        res = [dist(coor(g1(), g2()), coor(g3(), g4())) for _ in range(10000)]
        print(
            'P(dist(a1,a2) < R | R = 1) = ',
            sum(i < r for i in res) / len(res)
        )


class Task3(BasicGraph2D):
    """Задача 3."""

    def __call__(self):
        """Решение."""
        g1, g2, g3 = (ROOT.TRandom3(seed=(i * 42)).Rndm for i in range(1, 4))

        a = np.array([0, 0, 0])
        b = np.array([0, 1, 0])
        c = np.array([np.sqrt(3)/2, 1/2, 0])
        d = np.array([np.sqrt(3)/6, 1/2, np.sqrt(6)/3])
        e1, e2, e3 = b - a, c - b, d - c

        gen_xyz = (lambda g1, g2, g3: (
            a[0] + g1 ** (1/3) * (e1[0] + g2 ** (1/2) * (e2[0] + g3 * e3[0])),
            a[1] + g1 ** (1/3) * (e1[1] + g2 ** (1/2) * (e2[1] + g3 * e3[1])),
            a[2] + g1 ** (1/3) * (e1[2] + g2 ** (1/2) * (e2[2] + g3 * e3[2])),
        ))

        for i in range(super().ENTRIES):
            self.graph.SetPoint(i, *gen_xyz(g1(), g2(), g3()))


class Task4(BasicGraph):
    """Задача 4."""

    def __call__(self):
        """Решение."""
        x = [np.sqrt(10) * np.sqrt(5 + np.sqrt(5)) / 10
             * np.cos(-3 * np.pi / 10 + 2 * np.pi * i / 5)
             for i in range(2)]
        y = [np.sqrt(10) * np.sqrt(5 + np.sqrt(5)) / 10
             * np.sin(-3 * np.pi / 10 + 2 * np.pi * i / 5)
             for i in range(2)]
        e1 = np.array([x[0], y[0]])
        e2 = np.array([x[1], y[1]])
        e6 = e2 - e1

        r1, r2, r3 = (ROOT.TRandom3(seed=(42 * i)).Rndm for i in range(1, 4))

        for i in range(super().ENTRIES):
            g1, g2, g3 = r1(), r2(), r3()
            x = np.sqrt(g1) * (e1[0] + g2 * e6[0])
            y = np.sqrt(g1) * (e1[1] + g2 * e6[1])

            if 0.2 < g3 < 0.4:
                x, y = self._rotation(2 * np.pi / 5, np.array([x, y]))
            elif 0.4 < g3 < 0.6:
                x, y = self._rotation(4 * np.pi / 5, np.array([x, y]))
            elif 0.6 < g3 < 0.8:
                x, y = self._rotation(6 * np.pi / 5, np.array([x, y]))
            elif g3 > 0.8:
                x, y = self._rotation(8 * np.pi / 5, np.array([x, y]))

            self.graph.SetPoint(i, x, y)

    def _rotation(self, theta, arr):
        rot = np.array(
            [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
        )
        return np.dot(rot, arr)
