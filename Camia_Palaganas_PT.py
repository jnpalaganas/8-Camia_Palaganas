
# Jaelle Elyse Palaganas
# 8-Camia
# August 20, 2026

import math

# Pythagorean Theorem - a^2 + b^2 = c^2


# Ask user for the values of side a and side b

side_a = int(input(f"\nEnter the length of the side a: "))

side_b = int(input("Enter the length of the side b: "))


# Compute for a^2 and b^2 using pow()

a_squared = pow(side_a, 2)

b_squared = pow(side_b, 2)


# Get the sum of a^2 and b^2 for c^2

c_squared = a_squared + b_squared


# Square c^2 to get c, aka the hypotenuse using sqrt()

hypotenuse = math.sqrt(c_squared)


# Round the hypotenus to two decimal places for a clean result

hypotenuse = round(hypotenuse, 2)


# Display the Result

print(f"\nThe hypotenuse is: {hypotenuse}")