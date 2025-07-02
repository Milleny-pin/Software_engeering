print("Selecione as opções abaixo:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão") 

opcao_selecionada = input("Selecione uma opção: ")

n1 = input("Digite um número: ")
n2 = input("Digite um número: ")

print(f"Você selecionou a opção: {opcao_selecionada}")

if opcao_selecionada == 1:
    resultado = n1 + n2 
    print(f"O resultado é {resultado}")
