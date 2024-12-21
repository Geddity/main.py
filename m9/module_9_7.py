def is_prime(func):
    def wrapper(*args):
        value = func(*args)
        if value > 1:
            for i in range(2, int(value ** 0.5) + 1):
                if (value % i) == 0:
                    print("Составное")
            print("Простое")
        else:
            print("Составное")
        return value
    return wrapper

@is_prime
def sum_three(a, b ,c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)