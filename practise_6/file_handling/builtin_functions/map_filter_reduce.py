from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map() - square numbers
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

# filter() - even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even:", even)

# reduce() - sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print("Total:", total)

# built-in aggregation
print("Sum:", sum(numbers))
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Length:", len(numbers))