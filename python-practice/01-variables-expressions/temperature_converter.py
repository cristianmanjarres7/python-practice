#Conversor de temperatura de grados F a grados C
celsius = input("Enter the number of degrees Celsius to convert: ")
fahrenheit = float(celsius) * 9/5 + 32
print(f"{celsius}°C is equivalent to {fahrenheit:.2f}°F")