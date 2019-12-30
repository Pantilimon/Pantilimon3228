def eucl_greatestcommondivisor(a:int,b:int)->int:
    if(b==0):
        return a
    return eucl_greatestcommondivisor(b,a%b)
a = int(input())
b = int(input())

print(eucl_greatestcommondivisor(a,b))
