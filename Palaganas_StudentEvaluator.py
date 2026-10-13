# -------------------------------------------------------------------------------------------------------------
# Jaelle Elyse Palaganas
# 8 - Camia
# October 13, 2026
# -------------------------------------------------------------------------------------------------------------


def display_header(): # — Show the program title and a separator before inputs
    print("\nSTUDENT PERFORMANCE EVALUATOR\n")

def get_student_info(): #— Ask for the student name and three assessment scores
    name = input("Enter student name: ")
    assessment_1 = int(input("\nEnter assessment 1: "))
    assessment_2 = int(input("\nEnter assessment 2: "))
    assessment_3 = int(input("\nEnter assessment 3: "))
    return name, assessment_1, assessment_2, assessment_3

def evaluate_performance(assessment_1, assessment_2, assessment_3):
    average = (assessment_1 + assessment_2 + assessment_3) / 3

    if 90 <= average <= 100:
        performance = "Outstanding"
    elif 85 <= average < 90:
        performance = "Very Satisfactory"
    elif 80 <= average < 85:
        performance = "Satisfactory"
    elif 75 <= average < 80:
        performance = "Fairly Satisfactory"
    elif average < 75:
        performance = "Needs Improvement"

    return average, performance

def display_report(name, assessment_1, assessment_2, assessment_3, average, performance):
    print("\nSTUDENT PERFORMANCE REPORT")
    print(f"Student Name: {name}")
    print(f"Assessment Scores: {assessment_1}, {assessment_2}, {assessment_3}")
    print(f"Average Score: {average:.2f}")
    print(f"Performance: {performance}")

display_header()
get_student_info()
evaluate_performance(assessment_1, assessment_2, assessment_3)
display_report(name, assessment_1, assessment_2, assessment_3, average, performance)