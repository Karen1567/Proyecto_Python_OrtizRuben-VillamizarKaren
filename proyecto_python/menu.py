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
            print("2.actualizar camper")
            print("3.Actualizar camper")
            print("4.matricular camper")

            decisioncamper = int(input("elige"))
            print("--------------------------")
            if (decisioncamper==1): 
                file.crear_camper()
                
                        
            elif (decisioncamper==2):
                decisiondecamper = str(input("ingresa el id del Camper: "))
                nombre = str(input("ingresa el nombre actualizado: "))
                apellido1 = str(input("ingresa el primer apellido actualizado: "))
                apellido2 = str(input("ingresa el segundo apellido actualizado: "))
                direccion = str(input("ingresa la direccion del camper actualizado: "))
                telefono1 = str(input("ingresa el telefono celular actualizado: "))
                telefono2 = str(input("ingresa el telefono fijo actualizado: "))
                edad = str(input("ingresa la edad actualizado: "))
                if (edad<18):
                        acudiente = str(input("ingresa el acudiente: "))
            elif (decisioncamper==3):
                notadeestudiante=str(input("ingresa el id del camper: "))
            elif (decisioncamper==4):
                matriculascamper=str(input("ingresa el id del camper: "))
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

