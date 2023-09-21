# Escreva um programa que leia 3 números inteiros, calcule e escreva a média aritmética entre eles

numero1 = float(input('digite o primeiro número:'))
numero2 = float(input('digite o segundo número:'))
numero3 = float(input('digite o terceiro número:'))

media = (numero1 + numero2 + numero3) / 3

print(f'A média aritmética é {media:.2f}')