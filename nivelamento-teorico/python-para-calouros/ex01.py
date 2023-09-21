# construa um programa que leia uma temperatura em Fahrenheit e converta-a para Celsius. Sabe-se que: C = (F - 32) / 1.8

temperatura = input('Insira a temperatura em Fahrenheit: ')
calculo = (float(temperatura) - 32) / 1.8
print(f'O resultado é {calculo:.2f}°C')