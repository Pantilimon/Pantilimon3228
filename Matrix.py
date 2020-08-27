a = [0]
b = []
r = 0
ai = 0
aj = 0
while a[0] != 'end':
    a = input().split()
    if a[0] != 'end':
        for q in range(len(a)):
            a[q] = int(a[q])
        b.insert(r, a)
        r += 1
A = [[0 for j in range(len(b[0]))] for i in range(len(b))]
for i in range(1, len(b) - 1):
    for j in range(1, len(a) - 1):
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if abs(di) != abs(dj):
                        ai = i + di
                        aj = j + dj
                    else:
                        continue
                    A[i][j] += b[ai][aj]
for e in A:
    print(e)
