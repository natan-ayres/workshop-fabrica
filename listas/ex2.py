while True:
    print("1. Adcionar Tarefa")
    print("2. Executar fila de Tarefas")
    exec = int(input("3. Sair"))
    if exec == 1:
        pilha1 = str(input("Digite qual tarefa você quer adcionar a pilha de tarefas:"))
        pilha = []
        pilha.append(pilha1)
        resposta = input("Você quer adcionar mais tarefas? S/N")
        if resposta == "S":
            pilha2 = str(input("Digite qual tarefa você quer adcionar a pilha de tarefas:"))
            pilha.append(pilha2)
            resposta = input("Você quer adcionar mais tarefas? S/N")
            if resposta == "S":
                pilha3 = str(input("Digite qual tarefa você quer adcionar a pilha de tarefas:"))
                pilha.append(pilha3)
    if exec == 2:
        print(pilha)
        print(pilha.pop())
    if exec == 3:
        break
        
        

