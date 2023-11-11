lecturas_tienes = int(input("Cuantas lecturas de temperatura tienes? "))
contador = 0 
temp = 0
equivocadas=0
 
while contador < lecturas_tienes:
  contador +=1 
  temp= float(input("Inserta la temperatura  "))
  if temp >= 10 and temp <= 40:
    pass
  else:
    equivocadas+=1 
print("el sensor se equivoco", equivocadas)
porcentaje = (equivocadas *100) / lecturas_tienes
print("el porcentaje de error es",porcentaje)
