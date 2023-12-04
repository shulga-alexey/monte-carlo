# Monte-Carlo

## Установка и запуск

Для локальной установки:

    git clone git@github.com:shulga-alexey/monte-carlo.git

Для построения гистограмм здесь используется PyROOT:

    pip install pyroot

Чтобы запустить задание выполните:

    python3 main.py <номер ДЗ> <номер задачи> <подзадача(буква: a,b,...)>

Ответ на задание можно найти в `./img/hw<номер ДЗ>`.

## ДЗ№5 (задачи 1-8): файл hw5.py

**Задание №1 ::** Построить псевдослучайную последовательность методом вычетов для заданных g, M, m<sub>0</sub>.

![Image alt](https://github.com/shulga-alexey/monte-carlo/blob/main/img/hw5/Task1%20(A)%3A%20g%3D5%5E17%2C%20M%3D2%5E42%2C%20m%3D1.png)

![Image alt](https://github.com/shulga-alexey/monte-carlo/blob/main/img/hw5/Task1%20(B)%3A%20g%3D13%2C%20M%3D17%2C%20m%3D3.png)

**Задание №2 ::** Разыграть случайную величину по биномиальному закону Bi(12, 1/3) используя метод для конечных N.

![Image alt](https://github.com/shulga-alexey/monte-carlo/blob/main/img/hw5/Task2%20%3A%20Bi(12%2C%200.33).png)

**Задание №3 ::** Построить отрицательное биномиальное распределение Bi_Neg(10, 0.1).

![Image alt](https://github.com/shulga-alexey/monte-carlo/blob/main/img/hw5/Task3%20%3A%20Pascal(10%2C%200.1).png)

**Задание №4 ::** Построить распределение Пуассона Poisson(5).

![Image alt](https://github.com/shulga-alexey/monte-carlo/blob/main/img/hw5/Task4%20%3A%20Poisson(5%2C%200.1).png)

**Задание №5 ::** Сгенерировать M значений случайной величины g~U[0,1] и построить {Mg}.

![Image alt](https://github.com/shulga-alexey/monte-carlo/blob/main/img/hw5/Task5%20(A)%3A%20%5BM*gamma%5D.png)

![Image alt](https://github.com/shulga-alexey/monte-carlo/blob/main/img/hw5/Task5%20(B)%3A%20%7BM*gamma%7D.png)

**Задание №7 ::** Построить биномиальное распределение Bi(50, 1/3).

![Image alt](https://github.com/shulga-alexey/monte-carlo/blob/main/img/hw5/Task7%20%3A%20Bi(50%2C%200.33).png)

**Задание №8 ::** Построить распределение Пуассона с параметрами lambda={10, 20, 100}.

![Image alt](https://github.com/shulga-alexey/monte-carlo/blob/main/img/hw5/Task8%20(A)%3A%20Poisson(lambda%3D10).png)

![Image alt](https://github.com/shulga-alexey/monte-carlo/blob/main/img/hw5/Task8%20(B)%3A%20Poisson(lambda%3D20).png)

![Image alt](https://github.com/shulga-alexey/monte-carlo/blob/main/img/hw5/Task8%20(C)%3A%20Poisson(lambda%3D100).png)


## ДЗ№6 (задачи 1-8): файл hw6.py