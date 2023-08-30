class Animal:
    def __init__(self, animal, som):
        self.animal = animal
        self.som = som
    
    def __str__(self):
        return f'Animal: {self.animal} Som: {self.som}'
    
class Cachorro(Animal):
    def __init__(self, animal, latir):
        self.animal = animal
        self.latir = latir

    def __str__(self):
        return f'Animal: {self.animal} Som: {self.latir}'

class Gato(Animal):
    def __init__(self, animal, miar):
        self.animal = animal
        self.miar = miar

    def __str__(self):
        return f'Animal: {self.animal} Som: {self.miar}'

gato = Gato('Gato','Miau')
cao = Cachorro('Cachorro','Auuu')

print(gato.__str__())
print(cao.__str__())





