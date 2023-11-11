alexa_1 = input("Hola!, escribe algo ")
separacion = alexa_1.split()
tiempos = separacion.count("alexa")
print(tiempos)
if tiempos == 1:
  print("En que te puedo ayudar?")
elif tiempos >1:
  print("Relajate, solo tienes que nombrareme una vez!")
