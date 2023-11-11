cliente=str(input("entra un cliente?  (si/no)"))
acumulador = 0
contador = 0
total_c = 0
no_compraron = 0
que_compro=0
acumulador_v1 = 0
acumulador_v2 = 0
acumulador_v3 = 0
acumulador_v4 = 0
while cliente == "si":
  c = str(input("compra algo?  (si/no)"))
  if c == "si":
    acumulador +=1 
    que_compro = str(input("Que compro?  Varita de sauco [1]  varita de espino [2]  varita de sauce [3]  varita de acebo [4]"))
    if que_compro == "1":
      acumulador_v1 +=1
    elif que_compro == "2":
      acumulador_v2 +=1
    elif que_compro == "3":
      acumulador_v3 +=1
    elif que_compro == "4":
      acumulador_v4 +=1
  cliente=str(input("entra un cliente?  (si/no)"))
  total_c +=1
  no_compraron = total_c - acumulador

print("Los clientes que compraro son", acumulador)
print("Los clientes que no compraron", no_compraron)
print("El total de clinetes son", total_c)
print("Las varitas que se vendieron son:",acumulador_v1, "varita de sauco", acumulador_v2, "Varita de espino",
      acumulador_v3, "varita de sauce",  acumulador_v4, "varita de acebo" )

print("Bonito dia!!")

