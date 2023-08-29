vel= int(input("Velocidade do Carro:"))
vel2= int(80)
vel3= (vel - vel2) * 7
vel4= (vel - vel2)
if vel > vel2:
    print("Você foi multado em {}R$ por ter trafegado a {}km/h e você estava {}km/h acima do limite".format (vel3, vel, vel4))
else:
    print("Você não foi multado, pois estava abaixo da velocidade maxima")