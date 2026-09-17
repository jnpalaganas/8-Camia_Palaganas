# 3. Student ID Checker

import re

student_id = input("Enter Student ID: ")

pattern = r"\d{4}-\d{4}"

if re.fullmatch(pattern,student_id):

    print("Valid Student ID.")

else:

    print("Invalid Student ID.")