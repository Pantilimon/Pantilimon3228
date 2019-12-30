def str_base(val: int, b: int) -> str:
    """Shows value using number base, e.g. str_base(44027, 36)=='XYZ'"""
    if b not in range(2, 37):
        return "ERROR"
    output = ""
    while val != 0:
        arg=val%b # переход к новому основанию, начало( деление стобиоком)
        if arg < 10:
            output += chr(arg + ord('0'))
        else:
            output += (arg + ord('A') - 10)
        val //= b
    return ''.join(reversed(output)) #(т.к. новые знач мы кидали в конец строки, ну значит проитаем её справа на лево)

val = int(input())
b = int(input())

print(str_base(val, b))
