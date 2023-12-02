# Методы обработки экспериментальных данных в физике частиц

1. Код решений задач находится в файле [```hw_avg.py```](https://github.com/shulga-alexey/monte-carlo/blob/main/hw_avg.py).
2. Сгенерированные результаты можно найти в директории [```./img/hw_avg```](https://github.com/shulga-alexey/monte-carlo/tree/main/img/hw_avg).

## Задача 1
Пусть даны три точки (x,y), имеющие некоррелированные гауссовы ошибки (ex,ey). Используя метод максимального правдоподобия определить параметры наиболее вероятной прямой, проходящей через эти точки.

_Пояснения:_

Пусть  $`ex, ey ~ N(0, std^2)`$. Тогда учитывая $`y = a*x + b + ey`$, находим, что $`y ~ N(a*x + b, std^2)`$. Таким образом, для логарифма функции правдоподобия:

$`ln(L(a, b)) = \sum (-ln(2*pi)/2 - ln(std) - (dy_i/std)^2/2)`$, где $`dy_i = y_i - a*x_i - b`$

Некоторые результаты работы программы c различными параметрами:

![](https://github.com/shulga-alexey/monte-carlo/blob/main/img/hw_avg/Task1_1.png)

![](https://github.com/shulga-alexey/monte-carlo/blob/main/img/hw_avg/Task1_2.png)

![](https://github.com/shulga-alexey/monte-carlo/blob/main/img/hw_avg/Task1_3.png)
