Usuario_correcto = "admin"
Contraseña_correcta = "Admin2026"
Tarifa_inicial = 200
intentos = 0
acceso = 0

while intentos < 3:
    print("--INICIO DE SESION--")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario == "":
        print("El usuario no puede estar vacio")
        intentos += 1
        continue

    if not usuario.isalnum():
        print("El Usuarion no debe tener espacios")
        intentos += 1
        continue

    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres")
        intentos += 1
        continue

    if not any(c.isalpha() for c in contraseña) or not any(c.isdigit() for c in contraseña):
        print("La contraseña debe tener letras y numeros")
        intentos += 1
        continue

    if usuario == Usuario_correcto and contraseña == Contraseña_correcta:
        print("--BIENVENIDO--")
        acceso = 1
        break
    else:
        print("Los Datos son incorrectos")
        intentos += 1

while acceso == 1:
    print("\n" + "="*20)
    print("--MENU--")
    print("1. Clasificar numeros")
    print("2. Categoria de edad")
    print("3. Calcular tarifa")
    print("4. Cerrar sesion")
    print("5. Salir")
    print("="*20)

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        num_input = input("Ingresa un numero entero: ")
        if num_input.lstrip("-").isdigit():
            n = int(num_input)
            if n > 0: print("El numero es positivo")
            elif n < 0: print("El numero es negativo")
            else: print("El numero es cero")
            if n % 2 == 0: print("El numero es par")
            else: print("El numero es impar")
        else:
            print("Entrada no valida.")

    elif opcion == "2":
        print("--- Verificacion de Edad ---")
        edad_usr = int(input("Ingresa edad (0-120): "))
        
        if 0 <= edad_usr <= 120:
            identifica = input("¿Tienes identificacion? (s/n): ").lower()
            licencia = input("¿Tienes licencia? (s/n): ").lower()

            if edad_usr <= 12:
                print("Eres menor, Requieres un tutor")
            elif edad_usr <= 17:
                print("Eres un adolescente, Requieres un Tutor")
            elif edad_usr <= 64:
                print("Eres un Adulto")
                if edad_usr >= 21 and identifica == "s":
                    print("Acceso VIP concedido")
            else:
                print("Adulto mayor")
                if identifica == "s":
                    print("Acceso VIP concedido")

            if licencia == "s":
                print("Permiso autorizado para conducir")
            else:
                print("Permiso no autorizado para conducir")
        else:
            print("Rango de edad fuera de los limites.")

    elif opcion == "3":
        print("--Cotizador de Tarifa--")
        e = int(input("Edad: "))
        d = int(input("Día (1-7): "))
        est = input("¿Estudiante? (s/n): ").lower()
        mbr = input("¿Miembro? (s/n): ").lower()
        met = input("Método E(efectivo) / T(tarjeta): ").lower()

        desc = 0
        recar = 0.10 if d >= 6 else 0

        if e <= 12: desc += 0.50
        elif e <= 17: desc += 0.20
        elif e >= 65: desc += 0.30

        if est == "s" and e >= 13: desc += 0.15
        if mbr == "s": desc += 0.10
        if met == "e": desc += 0.05

        if desc > 0.60: desc = 0.60

        total = Tarifa_inicial * (1 - desc) * (1 + recar)
        print(f"Total a pagar: ${total:.2f}")

    elif opcion == "4":
        print("Cerrando sesion...")
        acceso = 0

    elif opcion == "5":
        print("Finalizando ejecucion...")
        intentos = 4 
        break
    else:
        print("Opcion invalida.")

if intentos == 3:
    print("Bloqueado: Demasiados intentos fallidos.")
elif intentos == 4:
    print("Gracias por usar el software.")
