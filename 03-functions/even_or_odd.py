# even_or_odd.py

def check_even_odd(number):
    return "Even number" if number % 2 == 0 else "Odd number"

number = int(input("Enter a number: "))
print(check_even_odd(number))