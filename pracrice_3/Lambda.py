x = lambda a : a + 10
print(x(5))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))



numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)



points = [(1, 2), (3, 1), (0, 5)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)



