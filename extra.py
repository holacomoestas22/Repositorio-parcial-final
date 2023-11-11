eventos = int(input("Ingresa el nuemero de eventos en el partido de quidditch "))
contador = 0
acumulador_1g =0
acumulador_2s = 0
puntos_1g 
while contador < eventos:
  contador +=1 
    
  equipo = str(input("Que equipo anoto? Gryffindor o Slytherin "))
  el_evento = str(input("Ingresa el evento (goal/snitch/foul)"))
  if equipo == "Gryffindor" and el_evento =="goal":
    suma_1= acumulador_1g + 10
  elif equipo == "Gryffindor" and el_evento =="snitch":
    suma_1 = acumulador_1g + 150 
  elif equipo == "Gryffindor" and el_evento =="foul":
    suma_1 = acumulador_1g - 30
    
  elif equipo == "Slytherin" and el_evento == "goal":
    suma_2 = acumulador_2s +10
  elif equipo == "Slytherin" and el_evento == "snitch":
    suma_2 = acumulador_2s +150
  elif equipo == "Slytherin" and el_evento == "foul":
    suma_2 = acumulador_2s - 30
