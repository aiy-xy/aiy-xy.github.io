import numpy as np
import matplotlib.pyplot as plt

while True:

    def plot_function():
        # Get the function from the user
        function_str = input("Enter the function: ")
        try:
            # Create a lambda function from the user input
            function = lambda x: eval(function_str)
        except:
            print("Invalid function!")
            return

        # Get the range of x values for plotting
        x_min = float(input("Enter the minimum x value: "))
        x_max = float(input("Enter the maximum x value: "))

        # Generate x values from the specified range
        x = np.linspace(x_min, x_max, 1000)

        # Evaluate the function for each x value
        y = function(x)

        # Create the plot
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')

        # Display the plot
        plt.show()

    # Call the function to start plotting
    plot_function()
