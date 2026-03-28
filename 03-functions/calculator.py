# Calculadora sencilla

def sumar (a,b):
    suma = a + b
    return f'El resultado final es: {suma}'

def restar (a,b):
    resta = a - b
    return f'El resultado final es: {resta}'

def multiplicar (a,b):
    multiplicacion = a * b
    return f'El resultado final es: {multiplicacion}'

def dividir (a,b):
    division = a / b
    return f'El resultado final es: {division}'

def potenciar (a,b):
    potenciacion = a ** b
    return f'El resultado final es: {potenciacion}'

a = float(input('Ingresar el primer numero: '))
b = float(input('Ingresar el segundo numbero: '))

calcular = print(sumar(a,b))