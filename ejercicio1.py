voltaje1 = int(input("Ingrese le voltaje 1: "))
voltaje2= int(input("Ingrese le voltaje 2: "))
voltaje3= int(input("Ingrese le voltaje 3: "))
voltaje4= int(input("Ingrese le voltaje 4: "))

promedio = (voltaje1 + voltaje2 + voltaje3 +voltaje4)/4

if promedio >220:
    print("ALTO VOLTAJE")
else:
    print("VOLTAJE CORRECTO")