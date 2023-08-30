class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f'Saudações {self.nome}, você é um {self.profissao} e sua idade é {self.idade}'
    
nome = input("Digite o seu nome:")
idade = int(input("Digite a sua idade:"))
profissao = input("Digite a sua profissão:")

pessoa = Pessoa(nome, idade, profissao)

a = pessoa.__str__()
print(a)
