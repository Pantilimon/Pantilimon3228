import random
def eucl_greatestcommondivisor(a:int,b:int)->int:#алгоритм евклида
    if(b==0):
        return a
    return eucl_greatestcommondivisor(b,a%b)
def rec(b:int, n:int)->int:#бинарное возведение в степень
    if n==0:
        return 1
    if n%2 == 0:
       return rec(b*b, n/2)
    else:
        return b*rec(b, n-1)
def chek_ferma(n:int)->bool:
    for i in range(5):
        a=random.randint(1,1000)
        while eucl_greatestcommondivisor(a,n)>1 :
            a=random.randint(1,1000)
        if rec(a,n-1)%n != 1 :
            return False
    return True
n = int(input())
print(check_ferma(n))
