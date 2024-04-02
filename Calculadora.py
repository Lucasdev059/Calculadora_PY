def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    else:
        return a/b
    
print("Selecione a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite a opção desejada (Opção 1/ Opção 2/ Opção 3/ Opção 4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == '1':
    print("Resultado: ", soma(num1, num2))
elif opcao == '2':
    print("Resultado: ", subtracao(num1, num2))
elif opcao == '3':
    print("Resultado: ", multiplicacao(num1, num2))
elif opcao == '4':
    print("Resultado: ", divisao(num1, num2))
else:
    print("Opção inválida. Por favor, selecione uma operação válida.")