

while True:
  
  opcion = int(input("1-Ingresar Datos\n2-Mostrar datos\n3-Salir\n"))

  match opcion:
    case 1:
      print("ingrese datos: ")
    case 2:
      print("mostrando datos...")
    case 3:
      print("gracias por usar el programa!!!")
      break
