
total2 = []
while True:
    num = int(input("Digite o número:"))
    total2.append(num)
    if num == 0:
        break
print("O total é {}".format (sum(total2)))