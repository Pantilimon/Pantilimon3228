def prime_check(n:int)->bool:
    """prime number check"""
    if n == 1:
        return False
    if n%2 == 0:
        return False
    i = 3
    while (n+2) > i*i:
        if (n%i) == 0:
            return False
        i+=2
    return True
            
n = int(input())
print(prime_check(n))
