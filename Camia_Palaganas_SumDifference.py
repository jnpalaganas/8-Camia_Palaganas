# ---------------------------------------------------------------------

# Jaelle Elyse Palaganas

# 8-Camia

# October 15, 2026

# ---------------------------------------------------------------------

# Ask user to input two numbers

number_one = int(input("Enter first number: "))

number_two = int(input("Enter second number: "))

# Create a function to calculate the sum of both numbers

def calculate_sum():

    sum = number_one + number_two

    print(f"\nSum: {sum}")

# Create a function to calculate the difference

def calculate_difference():

    difference = number_one - number_two

    print(f"Difference: {difference}")

# Call both functions

display_sum = calculate_sum()

display_difference = calculate_difference()