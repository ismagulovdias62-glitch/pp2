# generators.py

# 1. Custom Iterator
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


# 2. Generator Function
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# 3. Generator Expression
squares = (x * x for x in range(10))


if __name__ == "__main__":
    print("Countdown:")
    for num in CountDown(5):
        print(num)

    print("\nFibonacci:")
    for num in fibonacci(10):
        print(num)

    print("\nSquares:")
    for num in squares:
        print(num)