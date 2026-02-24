#programa de auntetnticacion con login y contraseña
usuario_correcto = "admin"
contraseña_correcta = "Admin2026"

intentos = 3

def validar_usuario(usuario):
    if not usuario: 
        return False
    if not usuario.isalnum():
        return False
    return True

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    
    tiene_letra = False
    tiene_numero = False

    for c in contraseña:
        if c.isalpha():
            tiene_letra = True
        if c.isdigit():
            tiene_numero = True

    return tiene_letra and tiene_numero


while intentos > 0:
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if (not validar_usuario(usuario) or 
        not validar_contraseña(contraseña) or
        usuario != usuario_correcto or
        contraseña != contraseña_correcta):
        
        intentos -= 1
        print(f"Incorrecto. Te quedan {intentos} intentos.")
    else:
        print("Bienvenido")
        break

if intentos == 0:
    print("Intentos terminados. Bloqueado.")
