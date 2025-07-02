# src/app.py

def executar_calculadora(opcao_selecionada_str, n1_str, n2_str):
    """
    Executa a lógica da calculadora com base nas entradas fornecidas.
    Retorna o resultado da operação ou uma mensagem de erro.
    """
    try:
        opcao_selecionada = int(opcao_selecionada_str)
        n1 = float(n1_str)
        n2 = float(n2_str)

        resultado = None

        if opcao_selecionada == 1:
            resultado = n1 + n2
        elif opcao_selecionada == 2:
            resultado = n1 - n2
        elif opcao_selecionada == 3:
            resultado = n1 * n2
        elif opcao_selecionada == 4:
            if n2 == 0:
                return "Erro: Não é possível dividir por zero." # Retorna a string de erro
            else:
                resultado = n1 / n2
        else:
            return "Erro: Opção inválida. Por favor, selecione 1, 2, 3 ou 4."

        return resultado # Retorna o resultado numérico
    except ValueError:
        return "Erro: Entrada inválida. Por favor, digite números válidos e uma opção numérica."
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}"

# O bloco if __name__ == "__main__": garante que o código abaixo
# só será executado quando o arquivo app.py for rodado diretamente,
# e não quando for importado como um módulo em outro arquivo (como o de teste).
if __name__ == "__main__":
    print("Selecione as opções abaixo:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao_selecionada_str = input("Selecione uma opção: ")
    n1_str = input("Digite o primeiro número: ")
    n2_str = input("Digite o segundo número: ")

    print(f"Você selecionou a opção: {opcao_selecionada_str}")

    # Chama a função principal e imprime o resultado
    resultado_final = executar_calculadora(opcao_selecionada_str, n1_str, n2_str)
    if isinstance(resultado_final, str) and resultado_final.startswith("Erro"):
        print(resultado_final)
    else:
        # Formata a saída para as operações, se não for um erro
        if int(opcao_selecionada_str) == 1:
            print(f"O resultado da Adição é: {resultado_final}")
        elif int(opcao_selecionada_str) == 2:
            print(f"O resultado da Subtração é: {resultado_final}")
        elif int(opcao_selecionada_str) == 3:
            print(f"O resultado da Multiplicação é: {resultado_final}")
        elif int(opcao_selecionada_str) == 4 and n2_str != '0':
            print(f"O resultado da Divisão é: {resultado_final}")