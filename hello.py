# Missão 1
nota = float(input("Digite a nota do aluno: "))

if nota >= 6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")

    # Missão 2
idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Você pode votar.")
else:
    print("Você não pode votar.")

    # Missão 3
nota = float(input("Digite a nota do aluno: "))

if 90 <= nota <= 100:
    print("Parabéns, você tirou A!")
elif 80 <= nota < 90:
    print("Muito bem, você tirou B.")
elif 70 <= nota < 80:
    print("Bom trabalho, você tirou C.")
elif 60 <= nota < 70:
    print("Fique atento, você tirou D.")
else:
    print("Estude um pouco mais, você tirou F.")

    # Missão 4
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
print(f"A soma dos números é: {soma}")

# Missão 5
senha = input("Digite a senha: ")

if senha == "Python123":
    print("Acesso permitido.")
else:
    print("Acesso negado.")

    # Missão 6
numero = 1

while numero <= 10:
    print(numero)
    numero += 1

    # Missão 7
numeros = [8, 3, 10, 1, 5]
numeros.sort()

print("Números em ordem crescente:", numeros)

# Missão 8
nomes = ("Ana", "Bruno", "Carla", "Daniel", "Eduardo")

print("Primeiro nome:", nomes[0])
print("Último nome:", nomes[-1])

# Missão 9
def dobro(numero):
    return numero * 2

num = int(input("Digite um número: "))
print(f"O dobro de {num} é {dobro(num)}")

# Missão 10
def contar_letras(nome):
    return len(nome)

nome = input("Digite um nome: ")
print(f"O nome {nome} tem {contar_letras(nome)} letras.")