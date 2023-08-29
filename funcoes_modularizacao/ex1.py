#escolhi os exercicios de operadores
import funcoes
from funcoes import predecessor, sucessor
    
num = int(input("Digite o número:"))

print("O número que vem depois de {} é {}".format (num, sucessor(num)))
print("O número que vem antes de {} é {}".format (num, predecessor(num)))
