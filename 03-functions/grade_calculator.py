# grade_calculator.py

def calculate_grade(score):
    if not 0.0 <= score <= 1.0:
        return "Error"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"


score = float(input("Enter score: "))
print(f"Your grade is: {calculate_grade(score)}")