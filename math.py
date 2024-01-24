import math

friends = 5

friends += 5
print(friends)

friends -= 5
print(friends)

friends *= 2
print(friends)

friends /= 2
friends = int(friends)
print(friends)

friends **= 2
print(friends)

remainder = friends % 3                     # resto da divisao
print(remainder)

round1 = round(math.pi)                     # pega o numeiro inteiro, sem as casas decimais
print(round1)

abs1 = abs(-4)                              # valor absoluto, independente se for negativo
print(abs1)

pow1 = pow(4, 3)                            # pow (elevado, a X )
print(pow1)

max1 = max(round1, abs1, pow1)              # max de x numeros
print(max1)

min1 = min(round1, abs1, pow1)              # min de x numeros
print(min1)

print(math.pi)                              # pi
print(math.e)                               # constante exponencial
print(math.sqrt())                          # raiz quadrada
print(math.ceil())                          # aredonda um numero com casas para cima  9.1 para 10
print(math.floor())                         # aredonda um numero com casas para baixo 9.9 para 9

