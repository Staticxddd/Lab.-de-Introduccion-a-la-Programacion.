# INICIO DE SESION

------------------------------------------------------------------------

## 1. Variables iniciales

Primero se definen algunas variables que controlan el programa.

-   intentos: guarda cuantos intentos de login se han hecho.
-   usuario_valido: usuario correcto para entrar.
-   password_valida: contraseña correcta.
-   sesion_activa: indica si el usuario ya inicio sesion.
-   ejecutando_programa: controla si el programa sigue corriendo.

Estas variables ayudan a controlar el flujo del programa.

------------------------------------------------------------------------

## 2. Ciclo principal del programa

El programa usa un ciclo while:

while ejecutando_programa:

Esto hace que todo el sistema siga funcionando hasta que el usuario
decida salir o se bloquee el acceso.

------------------------------------------------------------------------

## 3. Sistema de inicio de sesion

Dentro del programa hay otro ciclo:

while intentos \< 3 and not sesion_activa:

Este ciclo permite intentar iniciar sesion maximo 3 veces.

El usuario escribe: - usuario - contraseña

Despues se hacen algunas validaciones.

### Validacion del usuario

Se usa:

user_input.isalnum()

Esto revisa que el usuario solo tenga letras y numeros y no tenga
espacios.

### Validacion de la contraseña

Se revisan tres cosas:

-   que tenga al menos 8 caracteres
-   que tenga al menos una letra
-   que tenga al menos un numero

Para eso se usan funciones como:

any(c.isalpha() for c in pass_input) any(c.isdigit() for c in
pass_input)

------------------------------------------------------------------------

## 4. Verificacion de datos

Si no hubo errores se comparan los datos ingresados con los correctos.

if user_input == usuario_valido and pass_input == password_valida

Si coinciden: - el usuario entra al sistema - sesion_activa cambia a
True

Si no coinciden: - se suma un intento - se muestra cuantos intentos
quedan.

Si llega a 3 intentos, el programa se bloquea.

------------------------------------------------------------------------

## 5. Menu del sistema

Cuando el usuario entra aparece un menu con varias opciones:

1)  Clasificar numero
2)  Categoria de edad y permiso
3)  Calcular tarifa final
4)  Cerrar sesion
5)  Salir

El usuario elige una opcion escribiendo un numero.

------------------------------------------------------------------------

## 6. Opcion 1: Clasificar numero

El usuario ingresa un numero.

El programa revisa: - si es positivo - si es negativo - si es cero

Tambien revisa si es: - par - impar

Para saber si es par se usa:

num % 2 == 0

------------------------------------------------------------------------

## 7. Opcion 2: Categoria de edad

El usuario ingresa su edad.

El programa clasifica la edad en:

-   Niño (menos de 13)
-   Adolescente (13 a 17)
-   Adulto (18 a 64)
-   Mayor (65 o mas)

Tambien dice si puede entrar solo o si necesita tutor.

Si la edad es menor de 18 necesita tutor.

------------------------------------------------------------------------

## 8. Opcion 3: Calculo de tarifa

Aqui el programa calcula el precio final de un servicio.

El precio base es:

base = 200

Despues se preguntan varios datos:

-   dia de la semana
-   edad
-   si es estudiante
-   si es miembro
-   metodo de pago

### Recargo de fin de semana

Si el dia es sabado o domingo se agrega un 10% extra.

### Descuentos

El programa aplica descuentos segun varias condiciones.

Edad: - 0 a 12 → 50% - 13 a 17 → 20% - 65 o mas → 30%

Otros descuentos: - estudiante → 15% - miembro → 10% - pago en efectivo
→ 5%

Todos los descuentos se suman, pero hay un limite de 60%.

### Calculo final

Primero se calcula el descuento total y luego el precio final.

El programa muestra un pequeño recibo con: - precio base - recargo -
porcentaje de descuento - total a pagar

------------------------------------------------------------------------

## 9. Opcion 4: Cerrar sesion

Esta opcion cierra la sesion del usuario.

-   sesion_activa pasa a False
-   intentos se reinicia a 0

Esto permite volver al login.

------------------------------------------------------------------------

## 10. Opcion 5: Salir

Esta opcion termina el programa completamente cambiando:

ejecutando_programa = False