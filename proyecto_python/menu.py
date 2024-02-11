contador = 0 
categoria = {}
while (contador != 3):
    print("--------------------------")
    print("1.coordinador")
    print("2.trainer ")
    print("3. camper")
    print("4. salir")
    print("--------------------------")
    cargo = int(input("elige"))
    if(cargo==1):
        print("--------------------------")
        print("1.inscribir camper")
        print("2.actualizar camper")
        print("3.actualizar notas")
        print("4.matricular camper")

        decisioncamper = int(input("elige"))
        print("--------------------------")
        if (decisioncamper==1): 
            identificacion = int(input("ingresa el numero de identificación"))
            nombre = str(input("ingresa el nombre"))
            apellido1 = str(input("ingresa el primer apellido: "))
            apellido2 = str(input("ingresa el segundo apellido: "))
            direccion = str(input("ingresa la direccion del camper: "))
            telefono1 = int(input("ingresa el telefono celular: "))
            telefono2 = int(input("ingresa el telefono fijo: "))
            edad = int(input("ingresa la edad: "))
            if edad<18:
                acudiente = str(input("ingresa el acudiente: "))
        if (decisioncamper==2):
            decisiondecamper = str(input("escribe el id del camper: "))
            nombre = str(input("ingresa el nombre: "))
            apellido1 = str(input("ingresa el primer apellido: "))
            apellido2 = str(input("ingresa el segundo apellido: "))
            direccion = str(input("ingresa la direccion del camper: "))
            telefono1 = str(input("ingresa el telefono celular: "))
            telefono2 = str(input("ingresa el telefono fijo: "))
            edad = str(input("ingresa la edad: "))
            if (edad<18):
                acudiente = str(input("ingresa el acudiente: "))
        if (decisioncamper==3):
            notadeestudiante=str(input("ingresa el id del camper: "))
        if (decisioncamper==4):
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
            print ("noshe")
    if cargo==3:
        print("--------------------------")
        print("1.-10 puntos")
        print("------------------------- ")
        break
         
    if cargo==4:
        break
