nome1= ("João Abrantes")
nome2= ("João Maia")
nome3= ("Pedro")
nome= str(input("Digite o seu nome:"))
if nome == nome1:
    print("Oi eu sou João Abrantes!")
if nome == nome2:
    print("Oi eu sou João Maia!")
if nome == nome3:
    print("Oi eu sou Pedro!")
else:
    print("Oi eu sou {}!".format (nome))
