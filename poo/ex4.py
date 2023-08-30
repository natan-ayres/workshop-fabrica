class FormaGeometrica:
    def calcular_a_area(self, raio):
        return 3.14*(raio**2)
    
class Circulo(FormaGeometrica):
    pass

class Retangulo(FormaGeometrica):
    def calcular_a_area(self, base, altura):
        return base*altura

circulo = Circulo()
area = circulo.calcular_a_area(20)
print(area)

retangulo = Retangulo()
area = retangulo.calcular_a_area(5,10)
print(area)