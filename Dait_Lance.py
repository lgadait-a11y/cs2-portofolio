import math

# Get inputs from the user
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate distance using math.sqrt() and math.pow()
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Round to 2 decimal places
rounded_distance = round(distance, 2)

# Display the output
print("The distance between the two points is:", rounded_distance)

# Reflection:
# Using the math library simplifies code by providing pre-built functions like sqrt() and pow().
# Without it, we would have to write complex custom code to estimate square roots manually.

# I asked ai for explanation watched vids and to make it and I somewhat understand it but not fully understand it yet
