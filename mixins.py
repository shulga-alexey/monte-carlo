"""Миксины для классов Tasks."""
import time

import ROOT


class Basic:
    """Класс для создания гистограмм."""

    ENTRIES = 10000
    HW_NUM = 5

    def __init__(self, name, *histargs, **solargs):
        """Создаются экземпляры Canvas и Histogram, сохраняется гистограмма."""
        canvas = ROOT.TCanvas('Сanvas', 'Histogram', 200, 10, 700, 500)
        canvas.SetFillColor(42)
        canvas.GetFrame().SetFillColor(21)
        canvas.GetFrame().SetBorderSize(6)
        canvas.GetFrame().SetBorderMode(-1)

        self.histogram = ROOT.TH1F('Histogram', name, *histargs)
        self.histogram.SetFillColor(48)

        self(**solargs)

        self.histogram.Draw()

        canvas.Update()
        canvas.Print(f'./img/hw{self.HW_NUM}/{name}.png')

        time.sleep(4)
