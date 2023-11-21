"""Отвечает за запуск примеров заданий."""
from sys import argv

from hw5 import Task1, Task2, Task3, Task4, Task5, Task7, Task8

if argv[1] == '5':
    if argv[2] == '1':
        if argv[3] == 'a':
            Task1(5**17, 2**42, 1, 'Task1 (A): g=5^17, M=2^42, m=1', 100, 0, 1)
        elif argv[3] == 'b':
            Task1(13, 17, 3,  'Task1 (B): g=13, M=17, m=3', 100, 0, 1)
    elif argv[2] == '2':
        Task2(12, 1/3, 'Task2 : Bi(12, 0.33)', 12, 0, 12)
    elif argv[2] == '3':
        Task3(10, 0.1,  'Task3 : Pascal(10, 0.1)', 190, 10, 200)
    elif argv[2] == '4':
        Task4(5, 0.1,  'Task4 : Poisson(5, 0.1)', 20, 0, 20)
    elif argv[2] == '5':
        if argv[3] == 'a':
            Task5(10**6, 'Task5 (A): {M*gamma} 10^6', 100, 0, 10**6)
        elif argv[3] == 'b':
            Task5(10**7, 'Task5 (B): {M*gamma} 10^7', 100, 0, 10**7)
    elif argv[2] == '6':
        pass
    elif argv[2] == '7':
        Task7(50, 1/3, 'Task7 : Bi(50, 0.33)', 25, 5, 30)
    elif argv[2] == '8':
        if argv[3] == 'a':
            Task8(10, 'Task8 (A): Poisson(lambda=10)', 25, 0, 25)
        elif argv[3] == 'b':
            Task8(20, 'Task8 (B): Poisson(lambda=20)', 30, 5, 35)
        elif argv[3] == 'c':
            Task8(100, 'Task8 (C): Poisson(lambda=100)', 100, 50, 150)
