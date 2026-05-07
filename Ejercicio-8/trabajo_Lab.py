XD=True
while XD:
    print("1. Palabra 10 veces")
    print("2. Edad")
    print("3. Numeros Positivos")
    print("4. Numeros Negativos")
    print("5. Interes")
    print("6. Piramide")
    print("7. Tablas de Multiplicar")
    print("8. Triangulo")
    print("9. Login")
    print("10. Numeros Primos")
    print("11. Invertir la palabra")
    print("12. Contar")
    print("13. Escribe algo")
    opcion=input("Elige una opcion: ")
    match opcion:
        case "1":
            palabra=input("Ingresa la palabra: ")
            for i in range(10):
                print(palabra)
        case "2":
            edad=input("Ingresa tu edad: ")
            for i in range(1, int(edad)+1):
                print(i)
        case "3":
            positivo=int(input("Introduce el numero positivo: "))
            for i in range(positivo + 1):
                if i == 0:
                    print(i, end="")
                else:
                    print(f", {i}", end="")
        case "4":
            positivo=int(input("Introduce un numero positivo: "))
            for i in range(positivo, -1, -1):
                if i > 0:
                    print(i, end=", ")
                else:
                    print(i)
        case "5":
            cantidad=float(input("Introduce la cantidad de dinero: "))
            intereses=float(input("Introduce la tasa de intereses: "))
            años=int(input("Años: "))
            for i in range(1, años +1):
                cantidad=cantidad*(1+intereses/100)
                print("Capital al año", i, ":", cantidad)
        case "6":
            numero=int(input("Introduce numero: "))
            for i in range(1, numero+1):
                print("*"* i)
        case "7":
            i = 1
            while i <= 10:
                print("Tabla del ", i, "")
                j = 1
                while j <= 10:
                    resultado = i * j
                    print(i, "x", j, "=", resultado)
                    j = j + 1
                    i = i + 1
                    print("")
        case "8":
            triangulo=int(input("Introduce la altura del triangulo: "))
            for i in range(1, triangulo+ 1):
                for j in range(2 * i - 1, 0, -2):
                    print("*", end=" ")
                    print("")
        case "9":
            contraseña_real = "contraseña"
            intento = ""
            while intento!= contraseña_real:
                intento=input("Introduce la contraseña: ")
                if intento!= contraseña_real:
                    print("Contraseña incorrecta, vuelva a intentarlo")
                    print("Contraseña correcta, Bienvenido!")
        case "10":
            numero_primo=int(input("Introduce un numero: "))
            primo=True
            if numero_primo < 2:
                primo=False
            else:
                for i in range(2, numero_primo):
                    if numero_primo % i==0:
                        primo=False
                        if primo:
                            print(numero_primo, "es numero primo")
                else:
                    print(numero_primo, "no es numero primo")
        case "11":
            palabrota=input("Introduce una palabra: ")
            for i in range(len(palabrota) -1, -1, -1):
                print(palabrota[i])
        case "12":
            frase=input("Introduce una frase: ")
            letra=input("Introduce una letra: ")
            contador=0
            for caracter in frase:
                if caracter==letra:
                    contador=contador+1
                    print("La letra", letra, "aparece", contador, "veces en esta frase")
        case "13":
            palabrita=" "
            while palabrita!="Salir":
                palabrita=input("Escribe algo (Salir para terminar): ")
                if palabrita!="Salir":
                    print(palabrita)
                    print("Terminado")