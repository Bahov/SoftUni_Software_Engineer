a = int(input())
b = int(input())

def factorial_division(a, b):
    factorial_a = 1
    factorial_b = 1

    for i in range(1, a + 1):
        factorial_a *= i

    for j in range(1, b + 1):
        factorial_b *= j

    print(f"{factorial_a/factorial_b:.2f}")

factorial_division(a, b)