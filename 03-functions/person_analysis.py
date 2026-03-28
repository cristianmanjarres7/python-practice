# person_analysis.py

def analyze_person(age, state):
    if age < 13 and state == "happy":
        return "You are a happy child"
    elif age < 18 and state == "anxious":
        return "You are an anxious teenager"
    elif age < 65 and state == "tired":
        return "You are a tired adult"
    elif age >= 65 and state == "resting":
        return "You are a resting grandparent"
    else:
        return "You are a special person :)"

age = int(input("Enter your age: "))
state = input("Enter your current state: ").lower()

print(analyze_person(age, state))