def executar_calculadora_simples(opcao_selecionada_str, n1_str, n2_str):


    try:
        
        opcao_selecionada = int(opcao_selecionada_str)
        
        n1 = float(n1_str)
        n2 = float(n2_str)
    except ValueError:
        return "Erro: Entrada inválida. Verifique os números ou a opção."

    resultado = None

    if opcao_selecionada == 1:
        resultado = n1 + n2
    elif opcao_selecionada == 2: 
        resultado = n1 - n2
    elif opcao_selecionada == 3:
        resultado = n1 * n2
    elif opcao_selecionada == 4: 
        if n2 == 0:
            return "Erro: Não é possível dividir por zero."
        resultado = n1 / n2
    else:
        return "Erro: Opção inválida."


    return resultado


if __name__ == "__main__":
    
    print("Selecione as opções abaixo:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao_input = input("Selecione uma opção: ")
    num1_input = input("Digite um número: ")
    num2_input = input("Digite outro número: ")

    print(f"Você selecionou a opção: {opcao_input}")

    final_result = executar_calculadora_simples(opcao_input, num1_input, num2_input)
    print(f"O resultado é: {final_result}")

