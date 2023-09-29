import pandas as pd
import matplotlib.pyplot as plt

while True:
    # User inputs
    x_label = input("Enter the label for the x-axis: ")
    y_label = input("Enter the label for the y-axis: ")
    title = input("Enter the title: ")

    # Get user input for x and y data
    x_values_input = input(f"Enter data for the '{x_label}' (comma-separated): ")
    y_values_input = input(f"Enter data for the '{y_label}' (comma-separated): ")

    x_values = [float(value.strip()) for value in x_values_input.split(",")]
    y_values = [float(value.strip()) for value in y_values_input.split(",")]

    # Create DataFrame
    data = pd.DataFrame({x_label: x_values, y_label: y_values})

    # Scatter plot
    plt.scatter(data[x_label], data[y_label])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

