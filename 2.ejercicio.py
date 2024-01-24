B = int(input("ingrese la base\n:"))
A = int(input("ingrese la altura\n:"))
Area = (B * A)/2
if Area < 1000:
    print(f"el area de su triangulo equilatero es: {Area}")
else:
    print("el area de su triangulo es mayor a 1000")