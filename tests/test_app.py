import os
import sys

# Garante que o diretório src seja incluído no caminho de importação
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import executar_calculadora



# Testes para operações válidas
def test_adicao():
    assert executar_calculadora("1", "10", "5") == 15.0

def test_subtracao():
    assert executar_calculadora("2", "10", "5") == 5.0

def test_multiplicacao():
    assert executar_calculadora("3", "10", "5") == 50.0

def test_divisao():
    assert executar_calculadora("4", "10", "2") == 5.0

# Teste de divisão por zero
def test_divisao_por_zero():
    assert executar_calculadora("4", "10", "0") == "Erro: Não é possível dividir por zero."

# Teste de opção inválida
def test_opcao_invalida():
    assert executar_calculadora("5", "10", "5") == "Erro: Opção inválida. Por favor, selecione 1, 2, 3 ou 4."

# Teste de entrada inválida (letra em vez de número)
def test_entrada_invalida_n1():
    assert "Erro: Entrada inválida" in executar_calculadora("1", "abc", "5")

def test_entrada_invalida_n2():
    assert "Erro: Entrada inválida" in executar_calculadora("1", "10", "xyz")

def test_entrada_invalida_opcao():
    assert "Erro: Entrada inválida" in executar_calculadora("x", "10", "5")
