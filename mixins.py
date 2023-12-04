"""Миксины для классов Tasks."""
from array import array
from time import sleep

import numpy as np
import ROOT


class BasicHist:
    """Класс для создания гистограмм."""

    ENTRIES = 100000
    HW_NUM = 0

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

        sleep(4)


class BasicGraphErrors:
    """Базовый класс для отрисовки графика."""

    def __init__(self, name, points, errors):
        """Конструктор."""
        self.points = np.array(points)
        self.errors = np.array(errors)

        self.canvas = ROOT.TCanvas('c1', 'Graph', 200, 10, 700, 500)
        self.canvas.SetGrid()
        self.canvas.SetBorderSize(12)
        self.canvas.SetFillColor(42)

        self.graph = ROOT.TGraphErrors(
            3,
            array('f', self.points[:, 0]),
            array('f', self.points[:, 1]),
            array('f', self.errors[:, 0]),
            array('f', self.errors[:, 1])
        )
        self.graph.SetTitle('Linear graph: Y(X) = p1*X + p0')
        self.graph.SetLineColor(2)
        self.graph.SetLineWidth(2)
        self.graph.SetMarkerColor(2)
        self.graph.SetMarkerStyle(21)
        self.graph.GetXaxis().SetTitle('X title')
        self.graph.GetYaxis().SetTitle('Y title')

        self.graph_text = ROOT.TPaveText(0.67, 0.6, 0.87, 0.45, "NDC")
        self.graph_text.SetTextAlign(12)
        self.graph_text.SetFillColor(43)
        self.graph_text.AddText(' RED: Fit(pol1, L)')

        self.function = ROOT.TF1('fun1', '[0]*x+[1]', -100, 100)
        self.function.SetLineColor(4)
        self.function.SetLineWidth(2)

        self.function_text = ROOT.TPaveText(0.15, 0.6, 0.28, 0.5, "NDC")
        self.function_text.SetTextAlign(12)
        self.function_text.SetFillColor(43)
        self.function_text.AddText('BLUE: scipy')

        self()

        self.graph.Draw('AP')
        self.graph_text.Draw('same')
        self.function.Draw('same')
        self.function_text.Draw('same')

        self.canvas.Update()
        self.canvas.GetFrame().SetFillColor(0)
        self.canvas.GetFrame().SetBorderSize(12)
        self.canvas.Modified()
        self.canvas.Update()
        self.canvas.Print(f'./img/hw_awg/Task1_{name}.png')

        sleep(4)
