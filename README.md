Задание. Разработать алгоритм и реализовать программу для перевода арифметических выражений в постфиксную запись и их вычисление.
Для арифметических выражений допустимы операции: сложения, вычитания, умножения, деления.
Обращаем внимание, что арифметическое выражение может содержать идентификаторы, значения которых задаются при запуске.
Разработанная программа должна выводить:
-постфиксную запись выражения
-вычислять значение выражения по постфиксной записи
-вычислять значение средствами языка программирования.

Вариант 23: a+b+c+d*q*w*e-t/r+u*i*o*p/h/j+k+l/n/m
Тесты: 
1)
Введите выражение: a+b+c+d*q*w*e-t/r+u*i*o*p/h/j+k+l/n/m
Постфиксная запись: a b + c + d q * w * e * + t r / - u i * o * p * h / j / + k + l n / m / +
a = 1
b = 2
c = 3
d = 4
q = 5
w = 6
e = 7
t = 8
r = 9
u = 10
i = 11
o = 12
p = 13
h = 14
j = 15
k = 16
l = 17
n = 18
m = 19
Результат = 942.875104427736
--------------------
2)
Введите выражение: -(a)
Постфиксная запись: a -
a = 5
Результат = -5.0
--------------------
3)
Введите выражение: -(h+10.25)
Постфиксная запись: h 10.25 + -
h = 1
Результат = -11.25
--------------------
4)
Введите выражение: -7*(10-55.5)
Постфиксная запись: 7 10 55.5 - * -
Результат = 318.5
--------------------
5)
Введите выражение: a*(b*(c-d))
Постфиксная запись: a b c d - * *
a = 1
b = 5
c = 2
d = 7
Результат = -25.0
--------------------
6)
Введите выражение: a*(b*(c-d)
Некорректная запись
--------------------
7)
Введите выражение: 1515/0
Постфиксная запись: 1515 0 /
Деление на ноль запрещено!
--------------------
8)
Введите выражение: -15.5/j
Постфиксная запись: 15.5 j / -
j = 0
Деление на ноль запрещено!
--------------------
9)
Введите выражение: (j+5.1)-2
Постфиксная запись: j 5.1 + 2 -
j = 1
Результат = 4.1
--------------------
10)
Введите выражение: (9
Некорректная запись
--------------------
11)
Введите выражение: 7u10
Некорректная запись
--------------------
