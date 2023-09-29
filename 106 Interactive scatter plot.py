import plotly.express as px
import pandas as pd

# Prompt the user to enter the x-axis and y-axis names
x_axis_name = input("Enter the name for the x-axis: ")
y_axis_name = input("Enter the name for the y-axis: ")

# Prompt the user to enter the number of values
num_values = int(input("Enter the number of values: "))

# Create an empty DataFrame
data = pd.DataFrame(columns=[x_axis_name, y_axis_name])

# Prompt the user to enter the values
for i in range(num_values):
    x_value = input(f"Enter {x_axis_name} value for point {i + 1}: ")
    y_value = input(f"Enter {y_axis_name} value for point {i + 1}: ")
    data = data.append({x_axis_name: x_value, y_axis_name: y_value}, ignore_index=True)

# Create the scatter plot using Plotly Express
fig = px.scatter(data, x=x_axis_name, y=y_axis_name, title='Interactive Scatter Plot')
fig.show()
