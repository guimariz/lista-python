# Faça um Programa que peça dois números e imprima o maior deles. 
# Entrada: num1 e num2
# saida: maior número

num1 = int(input("Informe um número: "))
num2 = int(input("Informe um outro número: "))

if num1 < num2:
    maior_numero = f"O maior número é o {num2}"
elif num1 > num2:
    maior_numero = f"O maior número é o {num1}"
else:
    maior_numero = "Os dois números são iguais"

print(maior_numero)