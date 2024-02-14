import campers_CRUD as crud
import os

contador = 0 
categoria = {}
while (contador != 3):
    print("|==========================|")
    print("|        Bienvenido        |")
    print("|==========================|")
    print("| 1.coordinador")
    print("| 2.trainer ")
    print("| 3.camper")
    print("| 4. salir")
    print("____________________________")
    cargo = int(input("selecciona tu rol: "))
    if(cargo==1):
        print("_____________________________")
        print("1.Camper")
        print("2.Trainer")
        print("3.Rutas")
        print("4.notas")
        print("5.inicio")
        print("______________________________")
        ingreso = int(input("elige una opcion: "))
        if (ingreso == 1):
            print("______________________________")
            print("1.Inscribir camper")
            print("2.actualizar camper")
            print("3.matricular camper")
            print("4.listar campers")

            decisioncamper = int(input("elige una opcion: "))
            print("_______________________________")
            if (decisioncamper==1):
                crud.crear_camper()
                        
            elif (decisioncamper==2):
                crud.actualizar_camper()
            elif (decisioncamper==3):
                notadeestudiante=str(input("ingresa el id del camper: "))
            elif (decisioncamper==4):
                matriculascamper=str(input("ingresa el id del camper: "))
    if cargo==2:
        print("_____________________________")
        print("1.ingresa el horario")
        print("2.ver horario ")
        decisiondetrainers = int(input("ingresa la desicion con numeros: "))
        if decisiondetrainers ==1:
            horarioprofe1= str (input("ingresa hora de inicio"))
            horarioprofe2= str (input("ingresa hora de finalización"))
        if decisiondetrainers ==2:
            print ("noche")
    if cargo==3:
        print("|==========================|")
        print("|     No tienes acceso     |")
        print("|==========================|")
        break
    
         
    if cargo==4:
        break

