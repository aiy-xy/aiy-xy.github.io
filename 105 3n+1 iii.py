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

# Prompt the user to input the colors
line_color = input("Enter line color (e.g., 'blue', '#FF0000'): ")
marker_color = input("Enter marker color (e.g., 'green', '#00FF00'): ")

# Customize the graph appearance using user input colors
plt.plot(x, y, color=line_color, linestyle='-', linewidth=2, marker='o', markersize=5, markerfacecolor=marker_color)
plt.xlabel("Step")
plt.ylabel("Value")
plt.title("Collatz Sequence")
plt.grid(True)  # Add grid lines
plt.show()
