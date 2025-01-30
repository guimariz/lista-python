# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 
# entrada: valor
# saida: se é negativo ou positivo

num_list = [2, 10, 20, -1, -10]

for i, num in enumerate(num_list):
    if num < 0:
        print(f"A posição do número negativo é: {i + 1}")