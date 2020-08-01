
n = int(input('Digite um numero: '))

if n == 1:
    print("[0]")
elif n == 2:
    print("[0 1]")
else:
    v = [0]*n
    v[0] = 0
    v[1] = 1
    for x in range(2, n):
        v[x] = v[x-1] + v[x-2]
    print(v)
