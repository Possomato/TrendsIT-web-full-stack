# escreva um programa que leia duas notas de um aluno de programação. Em seguida, a média ponderada, com pesos 2 e 3, respectivamente, deve ser calculada. Por fim, O programa deve imprimir a média obtida

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

mediaPonderada = ((nota1 * 2) + (nota2 * 3)) / (2 + 3)

print(f'Sua nota final é {mediaPonderada:.2f}')

