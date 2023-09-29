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

x = list(range(len(sequence)))
y = sequence

# Customize the graph appearance
plt.plot(x, y, color='blue', linestyle='-', linewidth=2, marker='o', markersize=5)
plt.xlabel("Step")
plt.ylabel("Value")
plt.title("Collatz Sequence")
plt.grid(True)  # Add grid lines
plt.show()
