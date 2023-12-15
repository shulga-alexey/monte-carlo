"""Миксины для классов Tasks."""
import os
import time
from array import array

import numpy as np
import ROOT


class BasicHist:
    """Класс для создания гистограмм."""

    ENTRIES = 100000
    HW_NUM = None

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


class BasicHist2D:
    """Класс для создания 2D гистограмм."""

    def __init__(self):
        """Конструктор."""
        self.canvas = ROOT.TCanvas('Сanvas', 'Histogram', 200, 10, 700, 500)
        self.canvas.SetFillColor(42)
        self.canvas.SetFrameFillColor(33)
        self.canvas.SetBorderSize(6)
        self.canvas.SetBorderMode(-1)

        self.histogram = ROOT.TH2F(
            'DalitzHist', 'Dalitz Histogram', 40, 0, 2, 40, 0, 2
        )
        self.histogram.SetFillColor(48)
        self.histogram.SetMarkerStyle(6)
        self.histogram.SetXTitle(r'm^{2}_{23}')
        self.histogram.SetYTitle(r'm^{2}_{12}')

        self()

        self._save_img()
        # self._save_anim()

    def _save_anim(self):
        self.histogram.Draw('SURF3')
        self.canvas.Update()

        for i in range(10):
            self.canvas.SaveAs(f'./img/hw_avg/frame/frame{i}.png')
            self.canvas.SetPhi(96 + 36 * i)

        os.system(
            'convert -delay 250 -loop 0 '
            './img/hw_avg/frame/frame*.png ./img/hw_avg/Task2_2.gif'
        )

    def _save_img(self):
        self.histogram.Draw()
        self.canvas.Update()
        self.canvas.SaveAs('./img/hw_avg/Task2_1.png')


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

        self.function = ROOT.TF1('fun', '[0]*x+[1]', -100, 100)
        self.function.SetLineColor(4)
        self.function.SetLineWidth(2)

        self.test_function = ROOT.TF1('fun_test', '[0]*x+[1]', -100, 100)
        self.test_function.SetLineColor(28)
        self.test_function.SetLineWidth(2)

        self.graph_text = ROOT.TPaveText(0.67, 0.6, 0.9, 0.45, "NDC")
        self.graph_text.SetFillColor(43)
        self.graph_text.SetTextAlign(12)

        self.function_text = ROOT.TPaveText(0.15, 0.6, 0.38, 0.4, "NDC")
        self.function_text.SetFillColor(43)
        self.function_text.SetTextAlign(12)

        self.test_function_text = ROOT.TPaveText(0.15, 0.82, 0.38, 0.67, "NDC")
        self.test_function_text.SetFillColor(43)
        self.test_function_text.SetTextAlign(12)

        self()

        self.graph.Draw('AP')
        self.graph_text.Draw('same')
        self.function.Draw('same')
        self.function_text.Draw('same')
        self.test_function.Draw('same')
        self.test_function_text.Draw('same')

        self.canvas.Update()
        self.canvas.GetFrame().SetFillColor(0)
        self.canvas.GetFrame().SetBorderSize(12)
        self.canvas.Modified()
        self.canvas.Update()
        self.canvas.Print(f'./img/hw_avg/Task1_{name}.png')

        time.sleep(4)


class BasicGraph:
    """Базовый класс для отрисовки графика."""

    ENTRIES = 100000
    HW_NUM = None

    def __init__(self, name):
        """Конструктор."""
        self.graph = ROOT.TGraph()
        self.graph.SetTitle(name)
        self.graph.GetXaxis().SetTitle('X title')
        self.graph.GetYaxis().SetTitle('Y title')

        self()

        self.canvas = ROOT.TCanvas('c1', 'Graph', 200, 10, 700, 600)
        self.canvas.SetGrid()
        self.canvas.SetBorderSize(12)
        self.canvas.SetFillColor(42)

        self.graph.Draw('AP')
        self.canvas.Update()
        self.canvas.GetFrame().SetFillColor(0)
        self.canvas.GetFrame().SetBorderSize(12)
        self.canvas.Modified()
        self.canvas.Update()
        self.canvas.Draw()
        self.canvas.Print(f'./img/hw{self.HW_NUM}/{name}.png')

        time.sleep(5)


class BasicGraph2D:
    """Базовый класс для отрисовки трехмерного графика."""

    ENTRIES = 100000
    HW_NUM = None

    def __init__(self, name, **solargs):
        """Конструктор."""
        self.graph = ROOT.TGraph2D()
        self.graph.SetMargin(0.1)
        self.graph.SetTitle(name)
        self.graph.SetFillColor(48)

        self(**solargs)

        self.canvas = ROOT.TCanvas('Сanvas', 'Graph', 200, 10, 700, 500)
        self.canvas.SetFillColor(42)
        self.canvas.SetFrameFillColor(33)
        self.canvas.SetBorderSize(6)
        self.canvas.SetBorderMode(-1)

        self.graph.Draw('SURF3')
        self.canvas.Update()
        self.canvas.Print(f'./img/hw{self.HW_NUM}/{name}.png')

        time.sleep(10)
