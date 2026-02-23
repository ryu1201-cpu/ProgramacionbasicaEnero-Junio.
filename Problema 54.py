#Problema 54

nombres_ahorradores = ["Ana", "Luis", "María", "Carlos"]
ahorros = [500.00, 1500000.00, 950.00, 2000000.00]
for nom, ahorro in zip(nombres_ahorradores, ahorros):
    if ahorro < 1000:
        print(f"{nom} no tendrás para tu futuro")
    elif ahorro > 1000000:
        print(f"{nom} ya merito te retiras")
