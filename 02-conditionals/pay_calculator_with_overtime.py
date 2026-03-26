#Calculadora de pago con condicionales

hrs = input("Enter Hours: ")
h = float(hrs)

rate = input("Enter Rate: ")
r = float(rate)

if h <= 40:
    pay = h * r
else:
    extra = (h - 40) * r * 1.5
    pay = (40 * r) + extra

print(pay)