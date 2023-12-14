"""Отвечает за запуск примеров заданий."""
from sys import argv

import hw5
import hw6

if argv[1] == '5':
    if argv[2] == '1':
        if argv[3] == 'a':
            hw5.Task1('Task1 (A): g=5^17, M=2^42, m=1', 100, 0, 1,
                      g=5**17, M=2**42, m=1)
        elif argv[3] == 'b':
            hw5.Task1('Task1 (B): g=13, M=17, m=3', 100, 0, 1,
                      g=13, M=17, m=3)
    elif argv[2] == '2':
        hw5.Task2('Task2 : Bi(12, 0.33)', 12, 0, 12,
                  n=12, p=1/3)
    elif argv[2] == '3':
        hw5.Task3('Task3 : Pascal(10, 0.1)', 190, 10, 200,
                  n=10, p=0.1)
    elif argv[2] == '4':
        hw5.Task4('Task4 : Poisson(5, 0.1)', 20, 0, 20,
                  n=5, p=0.1)
    elif argv[2] == '5':
        if argv[3] == 'a':
            hw5.Task5('Task5 (A): [M*gamma]', 100, 0, 10**6,
                      M=10**6, intpart=True)
        elif argv[3] == 'b':
            hw5.Task5('Task5 (B): {M*gamma}', 100, 0, 1,
                      M=10**6, intpart=False)
    elif argv[2] == '7':
        hw5.Task7('Task7 : Bi(50, 0.33)', 25, 5, 30,
                  n=50, p=1/3)
    elif argv[2] == '8':
        if argv[3] == 'a':
            hw5.Task8('Task8 (A): Poisson(lambda=10)', 25, 0, 25,
                      lmbd=10)
        elif argv[3] == 'b':
            hw5.Task8('Task8 (B): Poisson(lambda=20)', 30, 5, 35,
                      lmbd=20)
        elif argv[3] == 'c':
            hw5.Task8('Task8 (C): Poisson(lambda=100)', 100, 50, 150,
                      lmbd=100)
elif argv[1] == '6':
    if argv[2] == '1':
        if argv[3] == 'a':
            hw6.Task1('Task1 (A): Exp(lmbd=1)', 200, 0, 10, lmbd=1)
        elif argv[3] == 'b':
            hw6.Task1('Task1 (B): Exp(lmbd=100)', 200, 0, 0.1, lmbd=100)
        elif argv[3] == 'c':
            hw6.Task1('Task1 (C): Exp(lmbd=1000)', 200, 0, 0.01, lmbd=1000)
    elif argv[2] == '3':
        if argv[3] == 'a':
            hw6.Task3('Task3 (A): HG(g=0)', 200, -1, 1, g=0)
        elif argv[3] == 'b':
            hw6.Task3('Task3 (B): HG(g=0.5)', 200, -1, 1, g=0.5)
        elif argv[3] == 'c':
            hw6.Task3('Task3 (C): HG(g=0.99)', 200, -1, 1, g=0.99)
    elif argv[2] == '5':
        hw6.Task5('Task5 : f(x) = a + b*x, a=1.5, b=-1', 100, 0, 1,
                  a=1.5, b=-1)
    elif argv[2] == '6':
        hw6.Task6('Task6 : f(x in (0,1)) = x, f(x in (1, 2)) = 2^(-x)',
                  200, 0, 2)
