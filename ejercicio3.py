voltaje1 = int(input("Ingrese el primer voltaje: "))
voltaje2= int(input("Ingrese el segundo voltaje: "))
voltaje3 = int(input("Ingrese el tercer voltaje: "))

promedio = (voltaje1+voltaje2+voltaje3)/3

if promedio <115:
    print("VOLTAJE CORRECTO")
elif promedio > 115 and promedio< 220:
    print("ALTO VOLTAJE")
elif promedio> 220:
    print("PELIGRO")