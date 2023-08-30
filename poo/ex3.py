class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return(f'Marca:{self.marca} Modelo: {self.modelo} Ano: {self.ano}')

class Velocidade(Carro):
    def velocidade(a):
        return a
    def aceleracao(velocidade, a):
        return (f"A velocidade agora é {velocidade + a}km/h")
    
carro = Carro('Volvo', 'Novo', '2023')
speed = Velocidade.velocidade(100)
print(carro)
print(f"A velocidade atual é: {speed}km/h")
acel = Velocidade.aceleracao(speed, 50)
print(acel)

    
        