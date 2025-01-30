# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe 
# contraram para desenvolver o programa que calculará os reajustes.

#     Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
#               baseado no salário atual:
#     salários até R$ 280,00 (incluindo) : aumento de 20%
#     salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#     salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#     salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#     o salário antes do reajuste;
#     o percentual de aumento aplicado;
#     o valor do aumento;
#     o novo salário, após o aumento. 

# Salário de um colaborador
# Saída:
# Salário antes do reajuste
# % de aumento aplicado
# o valor do aumento;
# o novo salário, após o aumento.

salario_colaborador = float(input("Informe o salário do colaborador:"))
aumento_salario = 0

if salario_colaborador <= 280:
    percentual_aplicado = 20
    aumento_salario = salario_colaborador * (percentual_aplicado / 100)
elif salario_colaborador <= 700:
    percentual_aplicado = 15
    aumento_salario = salario_colaborador * (percentual_aplicado / 100)
elif salario_colaborador <= 1500:
    percentual_aplicado = 10
    aumento_salario = salario_colaborador * (percentual_aplicado / 100)
else:
    percentual_aplicado = 5
    aumento_salario = salario_colaborador * (percentual_aplicado / 100)

print(f'Salário antes do reajuste era de: R${salario_colaborador:.2f}')
print(f'O percentual de aumento aplicado foi de: {percentual_aplicado:.2f}%')
print(f'O valor de aumento foi de: R${aumento_salario:.2f}')
print(f'O novo salário é de: R${aumento_salario + salario_colaborador:.99f}')