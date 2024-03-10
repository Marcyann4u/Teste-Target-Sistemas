def checkfibonacci(n, a=0, b=1, sequence=None):
    if sequence is None:
        sequence = [a, b]

    if n == a or n == b:
        return sequence, True

    c = a + b
    if c > n:
        return sequence, False

    sequence.append(c)
    return checkfibonacci(n, b, c, sequence)

number = 5
sequence, is_in_sequence = checkfibonacci(number)
print(f"Fibonacci: {sequence}")
print(f"O número {number} está na sequência de Fibonacci? {is_in_sequence}")
