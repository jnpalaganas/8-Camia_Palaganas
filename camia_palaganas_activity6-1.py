# 1. Payment Method Checker

payment_method = ["cash", "gcash", "card"]

payment = input("Enter your payment method: ")

if payment.lower() in payment_method:

    print("Valid payment method.")

else:

    print("Invalid payment method.")