def fibonacci_sequence(limit):
    """Prints a list containing the Fibonacci sequence up to the specified limit."""
    fibo = [0, 1]
    while fibo[-2] + fibo[-1] <= limit:
        fibo.append(fibo[-2] + fibo[-1])
    print(fibo)
fibonacci_sequence(50)
