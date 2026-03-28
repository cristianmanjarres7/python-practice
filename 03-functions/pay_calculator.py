# pay_calculator.py

def compute_pay(hours, rate):
    if hours <= 40:
        return hours * rate
    return (40 * rate) + ((hours - 40) * 1.5 * rate)


hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

print("Pay:", compute_pay(hours, rate))