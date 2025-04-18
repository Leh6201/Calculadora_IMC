# Projeto 1 - Calculadora de IMC

# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Entrada de dados do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Exibição do resultado
print(f"\nSeu IMC é: {imc:.2f}")

# Classificação do IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Você está com peso normal.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")
