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