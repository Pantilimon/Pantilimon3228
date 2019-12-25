def repeat(n):  # Вот это и надо реализовать (эта штука принимает переменную для декоратора)
    def decorator(func): #декоратор
        def fake(z): # декоратор создаёт фейковую функцию
            for i in range(n):  
                z = func(z)
            return z
        return fake # подменяем нашу функцию  на фейковую
    return decorator

@repeat(2)
def plus_1(x):
    return x + 1


@repeat(0)
def mul_2(x):
    return x * 2

print(plus_1(3))  # должно выдать 5
print(mul_2(4))  # должно выдать 4
