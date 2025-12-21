memoria = 0
def display(exibicao):
    print("          __________________________________________")
    print(f"                          {exibicao}")
    print("          |  _____________________________________  |")
    print("          | |                                     | |")
    print("          | |   7    8    9    /    C             | |")
    print("          | |                                     | |")
    print("          | |   4    5    6    *    √             | |")
    print("          | |                                     | |")
    print("          | |   1    2    3    -    %             | |")
    print("          | |                                     | |")
    print("          | |   0    .    =    +                  | |")
    print("          | |_____________________________________| |")
    print("          |_________________________________________|")

def insert_valor(valor):
    if valor == "C" or valor == "c":
        return "C"
    else:
        return float(valor)

def executar_calculos(memoria):
    display("Calculadora Simples")
    if memoria == 0:
        valor1 = insert_valor(input("Digite um valor: "))
    else:
        valor1 = memoria
    if valor1 == "C":
        return executar_calculos(0)
    display(valor1)
    operacao = input("Digite a operação (+, -, *, /, %, √): ")
    valor2 = insert_valor(input("Digite outro valor ou C: "))
    if valor2 == "C":
        return executar_calculos(0)
    calculo = 0
    if operacao == "+":
        calculo = valor1 + valor2
    elif operacao == "-":
        calculo = valor1 - valor2
    elif operacao == "*":
        calculo = valor1 * valor2
    elif operacao == "/":
        if valor2 != 0:
            calculo = valor1 / valor2
        else:
            calculo = print("Erro: Divisão por zero não é permitida.")
    elif operacao == "%":
        calculo = valor1 % valor2
    elif operacao == "√":
        if valor1 >= 0:
            valor2 = None  # Valor2 não é necessário para raiz quadrada
            calculo = valor1 ** 0.5
        else:
            calculo = print("Erro: Raiz quadrada de número negativo não é permitida.")
    else:
        calculo = print("Erro: Operação inválida.")
    return calculo

while True:
    resultado = executar_calculos(memoria)
    display(resultado)
    usar_memporia = input("Deseja usar o resultado como memória para o próximo cálculo? (s/n): ")
    while usar_memporia == "s" or usar_memporia == "S":
        display(resultado)
        resultado = executar_calculos(resultado)
        display(resultado)
        usar_memporia = input("Deseja usar o resultado como memória para o próximo cálculo? (s/n): ")