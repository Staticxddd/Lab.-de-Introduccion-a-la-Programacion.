intentos = 0
usuario_valido = "admin"
password_valida = "Admin2026"
sesion_activa = False
ejecutando_programa = True

while ejecutando_programa:
    while intentos < 3 and not sesion_activa:
        print("INICIAR SESION")
        user_input = input("Usuario: ")
        pass_input = input("Contraseña: ")

        error = False
        if not user_input.isalnum():
            print("El usuario no debe tener espacios")
            error = True
        
        tiene_letra = any(c.isalpha() for c in pass_input)
        tiene_num = any(c.isdigit() for c in pass_input)
        if len(pass_input) < 8 or not tiene_letra or not tiene_num:
            print("Contraseña debe tener minimo 8 caracteres, 1 letra y 1 digito.")
            error = True

        if not error:
            if user_input == usuario_valido and pass_input == password_valida:
                print(f"\n¡Bienvenido {user_input}!")
                sesion_activa = True
            else:
                intentos += 1
                print(f"Contraseña y Usuario Incorrectos. Intentos restantes: {3 - intentos}")
        
        if intentos == 3:
            print("Máximo de intentos alcanzado. BANEADO.")
            ejecutando_programa = False

    while sesion_activa:
        print("MENU")
        print("1) Clasificar numero")
        print("2) Categoria de edad y permiso")
        print("3) Calcular tarifa final")
        print("4) Cerrar sesion")
        print("5) Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            num = int(input("Ingrese un numero: "))
            res = "Positivo" if num > 0 else "Negativo" if num < 0 else "Cero"
            paridad = "Par" if num % 2 == 0 else "Impar"
            print(f"Resultado: {res} e {paridad}")

        elif opcion == "2":
            edad = int(input("Ingrese su edad: "))
            if edad < 13: cat = "Niño"
            elif edad < 18: cat = "Adolescente"
            elif edad < 65: cat = "Adulto"
            else: cat = "Mayor"
            permiso = "SÍ" if edad >= 18 else "NO (requiere tutor)"
            print(f"Categoria: {cat} | ¿Puede pasar solo?: {permiso}")

        elif opcion == "3":
            base = 200
            dia = int(input("Dia (1-Lun a 7-Dom): "))
            edad = int(input("Edad (0-120): "))
            estudiante = input("¿Estudiante? (S/N): ").upper()
            miembro = input("¿Miembro? (S/N): ").upper()
            pago = input("Metodo Pago: E (efectivo) / T (tarjeta): ").upper()

            recargo = base * 0.10 if dia >= 6 else 0

            desc_acumulado = 0
            if edad <= 12: desc_acumulado += 0.50
            elif edad <= 17: desc_acumulado += 0.20
            elif edad >= 65: desc_acumulado += 0.30

            if estudiante == "S" and edad >= 13:
                desc_acumulado += 0.15
            if miembro == "S":
                desc_acumulado += 0.10
            if pago == "E":
                desc_acumulado += 0.05

            if desc_acumulado > 0.60:
                desc_acumulado = 0.60

            descuento_total = (base + recargo) * desc_acumulado
            total = (base + recargo) - descuento_total

            print(f"\n--- RECIBO ---")
            print(f"Precio Base: ${base}")
            print(f"Recargo Fin de Semana: ${recargo}")
            print(f"% Descuento Aplicado: {desc_acumulado*100}%")
            print(f"TOTAL A PAGAR: ${total}")

        elif opcion == "4":
            print("Cerrando sesión...")
            sesion_activa = False
            intentos = 0 

        elif opcion == "5":
            print("Saliendo...")
            sesion_activa = False
            ejecutando_programa = False
        else:
            print("Opción no valida.")