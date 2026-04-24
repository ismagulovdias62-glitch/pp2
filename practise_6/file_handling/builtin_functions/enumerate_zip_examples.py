names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

# enumerate()
for index, name in enumerate(names):
    print(index, name)

# zip()
for name, score in zip(names, scores):
    print(name, score)

# sorted()
nums = [5, 2, 9, 1]
print("Sorted:", sorted(nums))

# type conversion
x = "123"
print("Type before:", type(x))

x = int(x)
print("Type after:", type(x))