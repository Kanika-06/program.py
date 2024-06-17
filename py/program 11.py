def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_numbers = generate_fibonacci(n)
print(f"The first {n} Fibonacci numbers are:")
print(fibonacci_numbers)
