intentos = 0
intentos_Maximos = 3
acceso_concedido = False
usuario_valido = "admin"
password_valido = "Admin2026"
ejecutando_programa = True

while ejecutando_programa:
    
    while intentos < intentos_Maximos and not acceso_concedido:
        print("INICIAR SESION")
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        valido = True   

        if usuario == "":
            print("El usuario no debe estar vacio")
            valido = False
        elif not usuario.isalnum():
            print("El usuario no debe tener espacios.")
            valido = False
        
        if len(contraseña) < 8:
            print("Contraseña debe tener minimo 8 caracteres.")
            valido = False

        tiene_letra = False
        for char in contraseña:
            if char.isalpha():
                tiene_letra = True
                break
        if not tiene_letra:
            print("La contraseña debe tener al menos una letra")
            valido = False

        tiene_numero = False
        for char in contraseña:
            if char.isdigit():
                tiene_numero = True
                break
        if not tiene_numero:
            print("La contraseña debe tener al menos un numero")
            valido = False

        if valido:
            if usuario == usuario_valido and contraseña == password_valido:
                print("Acceso permitido\n")
                acceso_concedido = True
            else:
                intentos += 1
                print("Datos incorrectos.")
                print("Tienes", intentos_Maximos - intentos, "intentos\n")
        else:
            print("Datos incorrectos, intenta de nuevo\n")

    if intentos == intentos_Maximos:
        print("Se alcanzo el numero de intentos permitidos. Programa terminado.")
        ejecutando_programa = False

    while acceso_concedido:
        print("---MENU---")
        print("1) Clasificar números")
        print("2) Categoría de edad y permisos")
        print("3) Calcular tarifa final")
        print("4) Cerrar sesión")
        print("5) Salir")
        opcion = input("Seleccione una opción: ")