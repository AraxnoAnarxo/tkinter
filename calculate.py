'''
Напишите простейший калькулятор, состоящий из двух текстовых полей,
куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/".
Результат вычисления должен отображаться в метке. Если арифметическое действие выполнить
невозможно (например, если были введены буквы, а не числа), то в метке должно
появляться слово "ошибка"
'''

#multiplication division subtraction addition

from tkinter import *

root = Tk()

e1 = Entry(width=20)
e2 = Entry(width=20)

b1 = Button(text='+')
b2 = Button(text='-')
b3 = Button(text='*')
b4 = Button(text='/')
l = Label(bg='black', fg='white',width=20)


# сложение
def addition(event):
    digit1 = e1.get()
    digit2 = e2.get()
    if digit1.isdigit() and digit2.isdigit():
        digit1= int(digit1)
        digit2 = int(digit2)
        res = digit1 + digit2
        l['text'] = res
    else:
        l['text'] = 'Ошибка'
# вычитание
def subtraction(event):
    digit1 = e1.get()
    digit2 = e2.get()
    if digit1.isdigit() and digit2.isdigit():
        digit1 = int(digit1)
        digit2 = int(digit2)
        res = digit1 - digit2
        l['text'] = res
    else:
        l['text'] = 'Ошибка'

# умножение
def multiplication(event):
    digit1 = e1.get()
    digit2 = e2.get()
    if digit1.isdigit() and digit2.isdigit():
        digit1 = int(digit1)
        digit2 = int(digit2)
        res = digit1 * digit2
        l['text'] = res
    else:
        l['text'] = 'Ошибка'

# деление
def division(event):
    digit1 = e1.get()
    digit2 = e2.get()
    try:
        if digit1.isdigit() and digit2.isdigit():
            digit1 = int(digit1)
            digit2 = int(digit2)
            res = digit1 / digit2
            l['text'] = res
        else:
            l['text'] = 'Ошибка'
    except ZeroDivisionError as z:
        l['text'] = f'Ошибка: {z}'



b1.bind('<Button-1>', addition)
b2.bind('<Button-1>', subtraction)
b3.bind('<Button-1>', multiplication)
b4.bind('<Button-1>', division)




e1.pack()
e2.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
l.pack()

root.mainloop()