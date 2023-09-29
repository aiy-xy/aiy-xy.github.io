# Twins in Time

import math

while True:
    # Prompt the user to input the duration of the journey in days
    journey_duration_days = float(input("How long will the journey take place, in days, please? "))

    # Prompt the user to input the fraction of the speed of light
    speed_fraction = float(input("Enter the fraction of the speed of light (e.g., 0.5 for half the speed of light): "))

    # Speed of light in m/s (approximately 299,792,458 m/s)
    c = 299792458.0

    # Calculate the time on Earth
    time_on_earth = journey_duration_days

    # Calculate the time dilation factor
    gamma = 1 / math.sqrt(1 - speed_fraction**2)

    # Calculate the time experienced by the fast twin traveling at the given speed
    time_on_fast_twin = time_on_earth / gamma

    # Print the results
    print("Time on Earth: {:.2f} days".format(time_on_earth))
    print("Time sensed by the fast twin: {:.2f} days".format(time_on_fast_twin))
    print ('')



    # Prompt the user to input the original length of the object (rest length) in meters
    rest_length = float(input("Enter the original length of the object in meters: "))

    # Prompt the user to input the velocity of the object in meters per second
    velocity = float(input("Enter the velocity of the object in meters per second (Speed of light in meters per second (approximately 299,792,458 m/s): "))

    # Speed of light in meters per second (approximately 299,792,458 m/s)
    c = 299792458.0

    # Calculate the Lorentz contraction factor
    gamma = 1 / math.sqrt(1 - (velocity**2 / c**2))

    # Calculate the contracted length
    contracted_length = rest_length / gamma

    # Print the results
    print("Original Length of the Object: {:.2f} meters".format(rest_length))
    print("Velocity of the Object: {:.2f} m/s".format(velocity))
    print("Contracted Length of the Object: {:.2f} meters".format(contracted_length))
    PRINT ('')
