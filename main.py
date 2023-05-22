print("Caixa Eletrônico")
print("\nNotas disponíveis: R$200, R$100, R$50, R$20 e R$10")
print("\nQUAL VALOR DESEJA SACAR? \n\n[1] R$50 \n[2] R$100 \n[3] R$250 \n[4] R$500 \n[5] R$1000 \n[6] Outro")
print("\nValor máximo de saque: R$ 2500")

option = int(input("\nDigite a opção que deseja: "))

while (option == 0) or (option > 6):
    print("Digite uma opção válida! ")
    print("\nQUAL VALOR DESEJA SACAR? \n\n[1] R$50 \n[2] R$100 \n[3] R$250 \n[4] R$500 \n[5] R$1000 \n[6] Outro")
    print("\nValor máximo de saque: R$ 2500")
    option = int(input("\nDigite a opção que deseja: "))

valor = 0

if option == 1:
    valor = 50
elif option == 2:
    valor = 100
elif option == 3:
    valor = 250
elif option == 4:
    valor = 500
elif option == 5:
    valor = 1000
elif option == 6:
    valor = int(input("Digite o valor que deseja sacar: "))
    while valor > 2500 or valor < 10 or (valor % 10 != 0):
        if valor > 2500:
            print("\nValor máximo de saque: R$ 2500")
        elif valor < 10:
            print("\nValor mínimo de saque: R$ 10")
        else:
            print("\nApenas valores terminados em 0 são aceitos")
        
        valor = int(input("Digite o valor que deseja sacar: "))


# Notas de 200
a = valor // 200
a2 = valor % 200

# Notas de 100
b = a2 // 100
b2 = a2 % 100

# Notas de 50
c = b2 // 50
c2 = b2 % 50

# Notas de 20
d = c2 // 20
d2 = c2 % 20

# Notas de 10
e = d2 // 10
e2 = d2 % 10

if valor >= 10:
    print("\nNotas a receber: ")
    print("")
if a > 0:
    print(a, "nota(s) de R$200")
if b > 0:
    print(b, "nota(s) de R$100")
if c > 0:
    print(c, "nota(s) de R$50")
if d > 0:
    print(d, "nota(s) de R$20")
if e > 0:
    print(e, "nota(s) de R$10")

print("\nOperação finalizada.")

##################################################################

# print("Caixa Eletrônico")
# print("\nNotas disponíveis: R$200, R$100, R$50, R$20 e R$10")
# print("\nValor máximo de saque: R$ 2500")
# valor = int(input("\nQUAL VALOR DESEJA SACAR? "))

# while valor > 2500:
#     print("\nValor máximo de saque: R$ 2500")
#     valor = int(input("\nQUAL VALOR DESEJA SACAR? "))

# while valor < 10:
#     print("\nValor mínimo de saque: R$ 10")
#     valor = int(input("\nQUAL VALOR DESEJA SACAR? "))

# a = valor // 200
# a2 = valor % 200

# b = a2 // 100
# b2 = a2 % 100

# c = b2 // 50
# c2 = b2 % 50

# d = c2 // 20
# d2 = c2 % 20

# e = d2 // 10
# e2 = d2 % 10

# if valor >= 10:
#     print("\nNotas a receber: ")

# if a > 0:
#     print(a, "nota(s) de R$200")

# if b > 0:
#     print(b, "nota(s) de R$100")

# if c > 0:
#     print(c, "nota(s) de R$50")

# if d > 0:
#     print(d, "nota(s) de R$20")

# if e > 0:
#     print(e, "nota(s) de R$10")

# print("\nOperação finalizada.")

