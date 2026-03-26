#Calculadora de notas
score = input('Enter score: ')
n = float(score)

if 0.0 <= n <= 1.0:
    if n >= 0.9:
        print('A')
    elif n >= 0.8:
        print('B')
    elif n >= 0.7:
        print('C')
    elif n >= 0.6:
        print('D')
    else:
        print('F')
else:
    print('Error')
    quit()