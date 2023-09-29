while True:
    import matplotlib.pyplot as plt
    import numpy as np

    function_str = input("Enter a function: ")

    # Create a function that takes a numpy array x and evaluates the function string for each element of x
    def evaluate_function(x):
        return eval(function_str)

    # Create an array of x values to evaluate the function at
    x = np.linspace(-1000000, 10, 100000000)

    # Evaluate the function at each x value to get an array of y values
    y = evaluate_function(x)

    # Create a plot of the function using matplotlib
    plt.plot(x, y)

    # Add axis labels and a title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of ' + function_str)

    # Show the plot
    plt.show()
    
