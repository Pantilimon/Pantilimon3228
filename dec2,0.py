def repeat(n): #столько раз поторим декоратор
    def decorator(genuine_function): #наш декоратор
        def fakefunc(args): # завели функцию, на которую подменим мосновную
            for i in range(n): # для всех повторений
                args = genuine_function(args) # присвоили аргументу значение начальной функции
            return args # вернули аргумент со значением нач функции в фейковую функцию
        return fakefunc # вернули её в декоратор
    return decorator # вернули декоратор и повторили ещё n-1 раз

@repeat(2)
def plus_1(x):
    return x + 1


@repeat(0)
def mul_2(x):
    return x * 2

print(plus_1(3))  # должно выдать 5
print(mul_2(4))  # должно выдать 4
