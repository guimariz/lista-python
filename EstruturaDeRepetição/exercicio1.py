# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 
# Entrada: uma nota válida
# Saída: Informação caso a nota seja invalida

nota = int(input("Informe uma nota: "))

while nota < 0 or nota > 10:
    print("A nota informada não é válida")
    nota = int(input("Informe novamente uma nota: "))

print("Valeu vadia")