while True:
    print("1. Adcionar Tarefa")
    print("2. Executar fila de Tarefas")
    exec = int(input("3. Sair"))
    if exec == 1:
        lista1 = str(input("Digite qual tarefa você quer adcionar a lista de tarefas:"))
        fila = []
        fila.append(lista1)
        resposta = input("Você quer adcionar mais tarefas? S/N")
        if resposta == "S":
            lista2 = str(input("Digite qual tarefa você quer adcionar a lista de tarefas:"))
            fila.append(lista2)
            resposta = input("Você quer adcionar mais tarefas? S/N")
            if resposta == "S":
                lista3 = str(input("Digite qual tarefa você quer adcionar a lista de tarefas:"))
                fila.append(lista3)
    if exec == 2:
        print(fila)
        print("Você tem que fazer esta tarefa:{}".format (fila[0]))
        fila.pop(0)
    if exec == 3:
        break
        
        

