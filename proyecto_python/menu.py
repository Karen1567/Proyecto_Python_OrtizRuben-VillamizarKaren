import funciones as file
contador = 0 
categoria = {}
while (contador != 3):
    print("--------------------------")
    print("-------Bienvenido---------")
    print("--------------------------")
    print("1.coordinador")
    print("2.trainer ")
    print("3.camper")
    print("4. salir")
    print("--------------------------")
    cargo = int(input("ingresa: "))
    if(cargo==1):
        print("--------------------------")
        print("1.Camper")
        print("2.Trainer")
        print("3.Rutas")
        print("4.notas")
        print("5.inicio")
        print("--------------------------")

        ingreso = int(input("elige"))
        if (ingreso == 1):
            print("--------------------------")
            print("1.Inscribir camper")
            print("2.Actualizar camper")
            print("3.matricular camper")
            print("4.cambiar estado camper")
            decisioncamper = int(input("elige"))
            print("--------------------------")
            
            if (decisioncamper==1): 
                file.crear_camper()

            elif (decisioncamper==2):
                file.actualizar_camper()

                #decisiondecamper = str(input("ingresa el id del Camper: "))
                #nombre = str(input("ingresa el nombre actualizado: "))
                #apellido1 = str(input("ingresa el primer apellido actualizado: "))
                #apellido2 = str(input("ingresa el segundo apellido actualizado: "))
                #direccion = str(input("ingresa la direccion del camper actualizado: "))
                #telefono1 = str(input("ingresa el telefono celular actualizado: "))
                #telefono2 = str(input("ingresa el telefono fijo actualizado: "))
                #edad = str(input("ingresa la edad actualizado: "))
                #acudiente = str(input("ingresa el acudiente: "))
            elif (decisioncamper==3):
                notadeestudiante=str(input("ingresa el id del camper: "))
            elif (decisioncamper==4):
                matriculascamper=str(input("ingresa el id del camper: "))
        if (ingreso == 3):
            print("--------------------------")
            print("1. Agregar ruta.")
            print("2. Modificar ruta.")
            print("4. Salir.")
            decisionRuta = int(input("Que desea realizar con las rutas? "))
            if (decisionRuta == 1):
                print("-"*80)
                print("Para agregar la nueva r uta indiquenos la informacion de los modulos. ")
                print("-"*80)
                print ("a. Introducción a la algoritmia.")
                print ("b. PSeInt")
                print ("c. Python.")
                intro = input(" >>> Fundamentos de programacion: ")
                print ("a. HTML.")
                print ("b. CSS")
                print ("c. Bootstrap.")
                web = input(" >>> Programación Web: ")
                print ("a. Java.")
                print ("b. JavaScript")
                print ("c. C#.")
                formal = input(" >>> Programación formal: ")
                print ("a. Mysql.")
                print ("b. MongoDb")
                print ("c. Postgresql.")
                bd = input(" >>> Bases de datos: ")
                print ("a. NetCore.")
                print ("b. Spring Boot")
                print ("c. NodeJS.")
                print ("d. Express.")
                backend = input(" >>> Backend: ")
                nombreRuta = input("Indique un nombre para esta ruta:  ")
                infModulos = {
                    "Fundamentos de programacion": intro,
                    "Programación Web": web,
                    "Programación formal": formal,
                    "Bases de datos": bd,
                    "Backend": backend
                }
                file.agregarRuta(infModulos,nombreRuta);
                
    if cargo==2:
        print("--------------------------")
        print("1.ingresa el horario")
        print("2.ver horario ")
        decisiondetrainers = int(input("ingresa la desicion con numeros: "))
        if decisiondetrainers ==1:
            horarioprofe1= str (input("ingresa hora de inicio"))
            horarioprofe2= str (input("ingresa hora de finalización"))
        if decisiondetrainers ==2:
            print ("noche")

    if cargo==3:
        print("--------------------------")
        print("no tienes acceso")
        print("------------------------- ")
        break
    
         
    if cargo==4:
        break

