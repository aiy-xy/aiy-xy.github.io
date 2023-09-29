def collatz(n):
    sequence = [n]  # Store the sequence of numbers
    while n != 1:
        if n % 2 == 0:  # If the number is even
            n = n // 2
        else:  # If the number is odd
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Example usage
number = int(input("Type a number: "))
sequence = collatz(number)
print(sequence)

import matplotlib.pyplot as plt

def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

number = int(input("Type a number: "))
sequence = collatz(number)

# Generate x and y coordinates for the graph
x = list(range(len(sequence)))
y = sequence

# Plot the sequence on a graph
plt.plot(x, y)
plt.xlabel("Step")
plt.ylabel("Value")
plt.title("Collatz Sequence")
plt.show()
