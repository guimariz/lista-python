# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações. 

nome_usuario = input("Informe o nome de usuário: ")
senha_usuario = input("Informe sua senha: ")

while nome_usuario == senha_usuario:
    print("Você informou o mesmo nome de usuário e senha, informe novamente!")
    nome_usuario = input("Informe o nome de usuário: ")
    senha_usuario = input("Informe sua senha: ")

print("Valeu vadia")