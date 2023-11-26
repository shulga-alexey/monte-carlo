"""Миксины для классов Tasks."""
import time

import ROOT


class Basic:
    """Класс для создания гистограмм."""

    ENTRIES = 10000
    HW_NUM = 5

    def __init__(self, name, *args):
        """Создаются экземпляры классов Canvas и  Histogram."""
        self.name = name

        self.canvas = ROOT.TCanvas('Сanvas', 'Histogram', 200, 10, 700, 500)
        self.canvas.SetFillColor(42)
        self.canvas.GetFrame().SetFillColor(21)
        self.canvas.GetFrame().SetBorderSize(6)
        self.canvas.GetFrame().SetBorderMode(-1)

        self.histogram = ROOT.TH1F('Histogram', name, *args)
        self.histogram.SetFillColor(48)

    def _get_histogram(self):
        """Сохраняется созданная гистограмма."""
        self.histogram.Draw()

        self.canvas.Update()
        self.canvas.Print(f'./img/hw{self.HW_NUM}/{self.name}.png')
<<<<<<< HEAD
=======

        time.sleep(4)
>>>>>>> origin/main
