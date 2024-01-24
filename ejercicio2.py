base = int(input("ingrese la base del triangulo: "))
altura = int(input("ingrese la altura del triangulo: "))

area = (base*altura)/2

if base != altura: 
    print(" el triangulo no es equilatero ")
    
elif area > 1000:
    print("DATOS NO VALIDOS")
else:
    print (f" el area del triangulo es {area}")