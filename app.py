print("Selecione as opções abaixo:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao_selecionada_str = input("Selecione uma opção: ")
n1_str = input("Digite o primeiro número: ")
n2_str = input("Digite o segundo número: ")

print(f"Você selecionou a opção: {opcao_selecionada_str}")

try:
    
    opcao_selecionada = int(opcao_selecionada_str)
    n1 = float(n1_str)
    n2 = float(n2_str)

    resultado = None 

    
    if opcao_selecionada == 1:
        resultado = n1 + n2
        print(f"O resultado da Adição é: {resultado}")
    elif opcao_selecionada == 2:
        resultado = n1 - n2
        print(f"O resultado da Subtração é: {resultado}")
    elif opcao_selecionada == 3:
        resultado = n1 * n2
        print(f"O resultado da Multiplicação é: {resultado}")
    elif opcao_selecionada == 4:
        if n2 == 0:
           
            print("Erro: Não é possível dividir por zero.")
        else:
            resultado = n1 / n2
            print(f"O resultado da Divisão é: {resultado}")
    else:
        
        print("Erro: Opção inválida. Por favor, selecione 1, 2, 3 ou 4.")

except ValueError:
    
    print("Erro: Entrada inválida. Por favor, digite números válidos e uma opção numérica.")
except Exception as e:
   
    print(f"Ocorreu um erro inesperado: {e}")