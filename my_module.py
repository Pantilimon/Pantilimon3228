def bez(x, y): # Коэффииенты Безу
    print('Коэффициенты будут присвоенны переменным k_0 и k_1 соотвественно')
    def GCD(a, b):
        a = int(a)
        b = int(b)
        if b == 0:
            return a
        return GCD(b, a % b)
    def egcd(c, d):
        gcd = GCD(c, d)
        for v in range(10 ** 3):
            for u in range(10 ** 3):
                if v * c + u * d == gcd:
                    return v, u, gcd
                if -v * c - u * d == gcd:
                    return -v, -u, gcd
                if -v * c + u * d == gcd:
                    return -v, u, gcd
                if v * c - u * d == gcd:
                    return v, -u, gcd
        return 'ERROR' 
    x = int(x)
    y = int(y)
    k = egcd(x, y)
    k_0 = k[0]
    k_1 = k[1]



def gcd(a, b): # НОД двух чисел
    a = int(a)
    b = int(b)
    if b == 0:
        return a
    return gcd(b, a % b)



def dec(func): # Декоратор
    def wrap(*args, **kwargs):
        res = func(*args, **kwargs)
        return res.upper()
    return wrap


  
def new_base(a, b): #Перевод числа a их 10-ной системы счисления в новую с.ч. b
    if b < 2:
        return "ERROR"
    output = ""
    while val != 0:
        arg = a % b
        if arg < 10:
            output += chr(arg + ord('0'))
        else:
            output += chr(arg + ord('A') - 10)
        a //= b
    return ''.join(reversed(output))



def prime_check(n): #Проверка числа на простоту
    import random
    def gcd(a,b):
        if b == 0:
            return a
        return gcd(b, a % b)
    def rec(b, n):
        if n == 0:
            return 1
        if n % 2 == 0:
           return rec(b*b, n/2)
        else:
            return b*rec(b, n-1)
    def check_ferma(n):
        for i in range(5):
            a = random.randint(1,1000)
            while gcd(a,n)>1 :
                a = random.randint(1,1000)
            if rec(a,n-1)%n != 1 :
                return False
        return True
    return check_ferma(n)



def gauss(A): #Метод Гаусса для реения системы линейных уравнений
    A = list(A)
    a = len(A[0])
    b = len(A)
    for k in range(0, a - 1): #По сути выбираем элементы глав. диагонали(те самый, на котрый буем делить)
        for q in range(k + 1, b): #Выбираем столбец, под элементом глав. диагонали, который мы выбрали выше
            for z in range(k, a): #Выбираем строку, начиная с элемента, индекс столбца которого равен индексу элемента на диагонаи
                w = A[q][k] / A[k][k]
                A[q][z] -= w * A[k][z]
    for l in range(b - 1, -1, - 1):
        for t in range(l - 1, -1, - 1):
            p = A[t][l] / A[l][l]
            A[t][a - 1] -= p * A[l][a - 1]
            A[t][l] = 0
    o = [0] * b
    for k in range(0, b): # Функция возваращает массив с решениями системы уравнений  
      o[k] = A[k][k]
    return(o)

