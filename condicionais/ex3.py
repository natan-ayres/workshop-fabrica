num = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digite o terceiro número:"))
if num > num2:
    if num > num3:
        if num2 > num3:
            print("O maior número é {} e o menor é {}".format (num, num3))
if num2 > num:
    if num2 > num3:
        if num3 > num:
            print("O maior número é {} e o menor é {}".format (num2, num))
if num3 > num:
    if num3 > num2:
        if num2 > num:
            print("O maior número é {} e o menor é {}".format (num3, num))
if num > num2:
    if num > num3:
        if num3 > num2:
            print("O maior número é {} e o menor é {}".format (num, num2))
if num2 > num:
    if num2 > num3:
        if num > num3:
            print("O maior número é {} e o menor é {}".format (num2, num3))
if num3 > num:
    if num3 > num2:
        if num > num2:
            print("O maior número é {} e o menor é {}".format (num3, num2))
if num3 == num2 == num:
    print("Os números são iguais")
if num > num2 and num3:
    if num2 == num3:
        print("O maior número é {}, porém os menores números empataram".format (num))
if num2 > num and num3:
    if num == num3:
        print("O maior número é {}, porém os menores números empataram".format (num2))
if num3 > num2 and num:
    if num2 == num:
        print("O maior número é {}, porém os menores números empataram".format (num3))


