#1
def square(a, b):
     return a * b

#2
def max_number(a, b):
    if a > b:
        return a
    return b

#3
def season(a):
    if a == 12 or a == 1 or a == 2:
        m = 'Зима'
    elif a == 3 or a == 4 or a == 5:
        m = 'Весна'
    elif a == 6 or a == 7 or a == 8:
        m = 'Лето'
    elif a == 9 or a == 10 or a == 11:
        m = 'Осень'
    return m

#4
def bank(a, y):
    for i in range(y):
        a = int(a+10*a/100)
    return a
