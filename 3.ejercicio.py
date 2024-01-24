v1 = int(input("ingrese el voltaje a calcular\n:"))
v2 = int(input("ingrese el voltaje a calcular\n:"))
v3 = int(input("ingrese el voltaje a calcular\n:"))
suma = v1+v2+v3
if suma < 115:
    print("voltaje correcto")
elif suma > 115 and suma <220:
    print("voltaje alto")
else:
    print("PELIGRO")