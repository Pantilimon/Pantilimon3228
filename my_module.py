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
