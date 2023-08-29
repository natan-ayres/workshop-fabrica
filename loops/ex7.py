
while True:
    contador_M = 1
    contador_F = 1
    while True:
        sexo = input("Digite M para Masculino, F para Feminino:")
        if sexo == "M":
            M = contador_M
            contador_M = M + 1
        elif sexo == "F":
            F = contador_F
            contador_F = F + 1
        elif sexo == "parar":
            print("A quantidade de F é: {} e a de M é {}".format (F, M))
            break
        else: 
            print("Nenhuma das opções foi atendida")
    