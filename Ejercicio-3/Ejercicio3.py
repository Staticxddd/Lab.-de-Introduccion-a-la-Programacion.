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

    if not validar_usuario(usuario):
        print("Usuario invalido. Debe ser alfanumerico y sin espacios.")
        continue

    if not validar_contraseña(contraseña):
        print("Contraseña invalida. Minimo 8 caracteres, 1 letra y 1 numero.")
        continue

    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("Bienvenido")
        break
    else:
        intentos -= 1
        print(f"Incorrecto. Te quedan {intentos} intentos.")

if intentos == 0:
    print("Intentos terminados. Bloqueado.")