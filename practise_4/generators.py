N = int(input())
def gene(N):
    for i in range(1, N+1):
        yield i**2
m = gene(N)
for i in m:
    print(i, end=" ")

D = [10, 20, 30]
s = iter(D)
for i in D:
    print(next(s))

