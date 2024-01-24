v1 = int(input("ingrese el voltaje a registrar\n:"))
v2= int(input("ingrese el voltaje a registrar\n:"))
v3= int(input("ingrese el voltaje a registrar\n:"))
v4= int(input("ingrese el voltaje a registrar\n:"))
v5= int(input("ingrese el voltaje a registrar\n:"))
suma = v1+v2+v3+v4+v5
if suma < 220:
    print(f"VOLTAJE CORRECTO {suma}")
else:
    print(f"ALTO VOLTAJE {suma}")