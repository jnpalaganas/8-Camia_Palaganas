# 5. Student score entry

exam_score = int(input("Enter Examination Score: "))

try:

    if 100 >= exam_score >= 0:

        print("Valid Examination Score.")

    else:

        print("Invalid input. Please enter a number between 0 and 100")

except ValueError:

    print("Invalid input. Please enter a number")