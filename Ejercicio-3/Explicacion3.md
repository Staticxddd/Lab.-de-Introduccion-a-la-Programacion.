# Login en Python

Es un login sencillo hecho en Python. Pide un usuario y una contraseña, valida que cumplan ciertas reglas y solo deja entrar si los datos son correctos.

Tambien limita a 3 intentos. Si fallas 3 veces... se bloquea.

------------------------------------------------------------------------

## ¿Que se hizo?

Primero agregamos los datos correctos en el código:

```
usuario_correcto = "admin"\
contraseña_correcta = "Admin2026"
```

Luego definimos que solo haya 3 intentos:

```
intentos = 3
```

------------------------------------------------------------------------

## Verificacion del Usuario

Se hizo una funcion para revisar que el usuario:

-   No este vacio
-   Solo tenga letras y numeros
-   No tenga espacios

```
def validar_usuario(usuario): if not usuario: return False if not
usuario.isalnum(): return False return True
```

------------------------------------------------------------------------

## Verificacion de la Contraseña

La contraseña debe cumplir:

-   Mínimo 8 caracteres
-   Al menos 1 letra
-   Al menos 1 numero

```
def validar_contraseña(contraseña): if len(contraseña) \< 8: return
False

    tiene_letra = False
    tiene_numero = False

    for c in contraseña:
        if c.isalpha():
            tiene_letra = True
        if c.isdigit():
            tiene_numero = True

    return tiene_letra and tiene_numero
```

------------------------------------------------------------------------

## Ciclo de Intentos

Se usa un while para repetir mientras haya intentos disponibles:

```
while intentos \> 0:
```

Si los valores estan mal:

```
intentos -= 1
```

Si llega a 0, el programa termina y muestra que no se tuvo acceso.

------------------------------------------------------------------------
