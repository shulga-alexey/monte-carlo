import ROOT
import time
# Создание TF1 объекта (функции)
func = ROOT.TF1("func", "sin(x)/x")



# Создание TGraph объекта
graph = ROOT.TGraph()
graph.SetPoint(0, 1, 1)
graph.SetPoint(1, 2, 2)
graph.SetPoint(2, 3, 3)
graph.SetPoint(3, 4, 4)

# Создание TCanvas объекта
canvas = ROOT.TCanvas("canvas", "canvas", 800, 600)

# Нарисовать функцию на графике

# Нарисовать график на том же графике
graph.Draw()
func.Draw('same')
canvas.Draw()

# Отображение графика
time.sleep(4)