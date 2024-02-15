import campersCRUD as file
contador = 0 
categoria = {}
while (contador != 3):
    print("=============================================")
    print("*   Bienvenido a Base de Datos Campusands   *")
    print("=============================================")
    print(" 1.coordinador")
    print(" 2.trainer ")
    print(" 3.camper")
    print(" 4.salir")
    print("---------------------------------------------")
    cargo = int(input("Selecciona tu Rol: "))
    file.limpiar_pantalla()
    if(cargo==1):
        print("=================================")
        print("*    Bienvenido Coordinador     *")
        print("=================================")
        print(" 1.Campers CRUD")
        print(" 2.Trainers")
        print(" 3.Rutas de aprendisaje")
        print(" 4.Notas CRUD")
        print(" 5.Volver al Inicio")
        print("--------------------------")
        ingreso = int(input("Elige: "))
        file.limpiar_pantalla()
        if (ingreso == 1):
            print("--------------------------")
            print(" 1.Inscribir camper")
            print(" 2.Actualizar camper")
            print(" 3.Matricular camper")
            print(" 4.Cambiar estado camper")
            print(" 5.Volver al Inicio")
            print("---------------------------")
            decisioncamper = int(input("Elige: "))
            print("-----------------------------")
            file.limpiar_pantalla()
            if (decisioncamper==1): 
                print("|===============================|")
                print("|      Datos Nuevo Camper       |")
                print("|===============================|")
                file.crear_camper()
                file.limpiar_pantalla()

            elif (decisioncamper==2):
                file.actualizar_camper()
                file.limpiar_pantalla()
                
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
        print("===================================")
        print("*      Bienvenido Trainer         *")
        print("===================================")
        print("1.Ingresar Nuevo horario")
        print("2.Ver Horarios ")
        print("3.Volver al Inicio")
        print("---------------------------")
        decisiondetrainers = int(input("Selecciona una opcion #: "))
        file.limpiar_pantalla()
        if decisiondetrainers == 1:
            horarioprofe1= str (input("Ingresa hora de inicio de clase: "))
            horarioprofe2= str (input("Ingresa hora de finalización de clase: "))
            file.limpiar_pantalla()
        if decisiondetrainers == 2:
            print ()
            file.limpiar_pantalla()
    if cargo==3:
        print("           ==================================          ")
        print("           *    HEY! NO Tienes Accesso      *          ")
        print("           ==================================          ")
        input("Presiona Cualquier boton para volver al menu Inicio:  ")
        file.limpiar_pantalla()
    if cargo==4:
        break