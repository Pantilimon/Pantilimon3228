def eucl_greatestcommondivisor(a:int,b:int)->int:
    """используя алг евкл надём gcd"""
    if(b==0):
        return a
    return eucl_greatestcommondivisor(b,a%b)

def egcd(c: int, d: int) -> int:
    gcd = eucl_greatestcommondivisor(c, d)
    """по определению коэф безу"""
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
    return 'ERROR' #Если коэф в Z не суз=ществуют

x = int(input())
y = int(input())

k = egcd(x, y)

print(k[0], k[1])
