#Menu
menuprincipal=int(input('Menu principal de miscelania: \n 1.Operadores \n 2.Condicionales \n 3.Ciclos \n 99.Salir \n'))
while menuprincipal != 99:
    if menuprincipal ==1:
        print ('operadores')
        operadores=int(input('\n 1.Calcular el área de un triángulo \n 2.Ingresar dos números por teclado y sumarlos \n 3.Ingresar un número y visualizar el número elevado al cuadrado. \n 4.Escribir un algoritmo que convierta de euros a dólares. \n 5.Escribir un algoritmo que pida el lado de un cuadrado y muestre el valor del área y del perímetro \n 6.Escribir un algoritmo que determine el área y el volúmen de un cilindro \n 7.Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y el área (pi*r)^2 del círculo inscrito. \n 8.Calcular el promedio de tres (3) números ingresados por teclado. \n 9.Devolver al menu anterior \n'))
        while operadores != 9:
            if operadores ==1:
                print("Calcular el area de un triangulo")
                base=float(input("Cual es la base: "))
                altura=float(input("Cual es la altura: "))
                area= base* altura/ 2.0
                print ("El resultado es: " ,area)         
                operadores=int(input('\n 1.Calcular el área de un triángulo \n 2.Ingresar dos números por teclado y sumarlos \n 3.Ingresar un número y visualizar el número elevado al cuadrado. \n 4.Escribir un algoritmo que convierta de euros a dólares. \n 5.Escribir un algoritmo que pida el lado de un cuadrado y muestre el valor del área y del perímetro \n 6.Escribir un algoritmo que determine el área y el volúmen de un cilindro \n 7.Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y el área (pi*r)^2 del círculo inscrito. \n 8.Calcular el promedio de tres (3) números ingresados por teclado. \n 9.Devolver al menu anterior \n'))
            elif operadores ==2:
                print ("Ingresar dos números por teclado y sumarlos")
                Num1=int(input('Ingrese primer numero: '))
                Num2=int(input('Ingrese segundo numero: '))
                print('El resultado es: ' ,Num1+Num2)
                operadores=int(input('\n 1.Calcular el área de un triángulo \n 2.Ingresar dos números por teclado y sumarlos \n 3.Ingresar un número y visualizar el número elevado al cuadrado. \n 4.Escribir un algoritmo que convierta de euros a dólares. \n 5.Escribir un algoritmo que pida el lado de un cuadrado y muestre el valor del área y del perímetro \n 6.Escribir un algoritmo que determine el área y el volúmen de un cilindro \n 7.Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y el área (pi*r)^2 del círculo inscrito. \n 8.Calcular el promedio de tres (3) números ingresados por teclado. \n 9.Devolver al menu anterior \n'))
            elif operadores ==3:
                print ('Ingresar un número y visualizar el número elevado al cuadrado')
                numero=int(input('Ingrese un numero: '))
                print('El numero elevado al cuadrado es: ' ,numero*numero)
                operadores=int(input('\n 1.Calcular el área de un triángulo \n 2.Ingresar dos números por teclado y sumarlos \n 3.Ingresar un número y visualizar el número elevado al cuadrado. \n 4.Escribir un algoritmo que convierta de euros a dólares. \n 5.Escribir un algoritmo que pida el lado de un cuadrado y muestre el valor del área y del perímetro \n 6.Escribir un algoritmo que determine el área y el volúmen de un cilindro \n 7.Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y el área (pi*r)^2 del círculo inscrito. \n 8.Calcular el promedio de tres (3) números ingresados por teclado. \n 9.Devolver al menu anterior \n'))
            elif operadores ==4:
                print ('Conversor de euros a dolares')
                euro=int(input('Escribe valor en euros para covertir en dolares:'))
                dolar=euro*1.10
                print('euro=' , dolar)
                operadores=int(input('\n 1.Calcular el área de un triángulo \n 2.Ingresar dos números por teclado y sumarlos \n 3.Ingresar un número y visualizar el número elevado al cuadrado. \n 4.Escribir un algoritmo que convierta de euros a dólares. \n 5.Escribir un algoritmo que pida el lado de un cuadrado y muestre el valor del área y del perímetro \n 6.Escribir un algoritmo que determine el área y el volúmen de un cilindro \n 7.Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y el área (pi*r)^2 del círculo inscrito. \n 8.Calcular el promedio de tres (3) números ingresados por teclado. \n 9.Devolver al menu anterior \n'))
            elif operadores ==5:
                print ("Calcular el area y perimetro de un cuadrado")
                lado=float(input("Digite la medida del lado: "))
                area= lado* lado
                print ("El area del cuadrado es: " ,area)
                perimetro= lado + lado+ lado + lado
                print('El perimetro del cuadrado es: ' ,perimetro)
                operadores=int(input('\n 1.Calcular el área de un triángulo \n 2.Ingresar dos números por teclado y sumarlos \n 3.Ingresar un número y visualizar el número elevado al cuadrado. \n 4.Escribir un algoritmo que convierta de euros a dólares. \n 5.Escribir un algoritmo que pida el lado de un cuadrado y muestre el valor del área y del perímetro \n 6.Escribir un algoritmo que determine el área y el volúmen de un cilindro \n 7.Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y el área (pi*r)^2 del círculo inscrito. \n 8.Calcular el promedio de tres (3) números ingresados por teclado. \n 9.Devolver al menu anterior \n'))
            elif operadores ==6:
                print('Calcular el area y volumen de un cilindro')
                radio= float(input('Escriba el radio del cilindro:'))
                altura= float(input('Escriba la altura del cilindro:'))
                area= 2 * 3.1416 * radio ** 2 + 2 * 3.1416 * radio * altura
                volumen= 3.1416 * radio **2 * altura
                print('El area del cilindro es: ' , area)
                print('El volumen del cilindro es: ' , volumen)
                operadores=int(input('\n 1.Calcular el área de un triángulo \n 2.Ingresar dos números por teclado y sumarlos \n 3.Ingresar un número y visualizar el número elevado al cuadrado. \n 4.Escribir un algoritmo que convierta de euros a dólares. \n 5.Escribir un algoritmo que pida el lado de un cuadrado y muestre el valor del área y del perímetro \n 6.Escribir un algoritmo que determine el área y el volúmen de un cilindro \n 7.Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y el área (pi*r)^2 del círculo inscrito. \n 8.Calcular el promedio de tres (3) números ingresados por teclado. \n 9.Devolver al menu anterior \n'))
            elif operadores ==7:
                print('Calcular el area y la longitud de la circunferencia')
                radio= float(input('Escriba el radio del circulo:'))
                area= 3.1416 * radio**2
                longitud= 2 * 3.1416 * radio
                print('El area del circulo es: ' , area)
                print('La longitud de la circunferencia es: ' , longitud)
                operadores=int(input('\n 1.Calcular el área de un triángulo \n 2.Ingresar dos números por teclado y sumarlos \n 3.Ingresar un número y visualizar el número elevado al cuadrado. \n 4.Escribir un algoritmo que convierta de euros a dólares. \n 5.Escribir un algoritmo que pida el lado de un cuadrado y muestre el valor del área y del perímetro \n 6.Escribir un algoritmo que determine el área y el volúmen de un cilindro \n 7.Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y el área (pi*r)^2 del círculo inscrito. \n 8.Calcular el promedio de tres (3) números ingresados por teclado. \n 9.Devolver al menu anterior \n'))
            elif operadores ==8:
                print('Calcular el promedio de tres (3) números ingresados por teclado')
                num1=int(input('Ingrese el primer numero:'))
                num2=int(input('Ingrese el segundo numero:'))
                num3=int(input('Ingrese el tercer numero:'))
                promedio= (num1 +num2 +num3) / 3
                print('El promedio de los numeros es:' , promedio)
                operadores=int(input('\n 1.Calcular el área de un triángulo \n 2.Ingresar dos números por teclado y sumarlos \n 3.Ingresar un número y visualizar el número elevado al cuadrado. \n 4.Escribir un algoritmo que convierta de euros a dólares. \n 5.Escribir un algoritmo que pida el lado de un cuadrado y muestre el valor del área y del perímetro \n 6.Escribir un algoritmo que determine el área y el volúmen de un cilindro \n 7.Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y el área (pi*r)^2 del círculo inscrito. \n 8.Calcular el promedio de tres (3) números ingresados por teclado. \n 9.Devolver al menu anterior \n'))
            else:
                print('Digitaste una opcion incorrecta')
                operadores=int(input('\n 1.Calcular el área de un triángulo \n 2.Ingresar dos números por teclado y sumarlos \n 3.Ingresar un número y visualizar el número elevado al cuadrado. \n 4.Escribir un algoritmo que convierta de euros a dólares. \n 5.Escribir un algoritmo que pida el lado de un cuadrado y muestre el valor del área y del perímetro \n 6.Escribir un algoritmo que determine el área y el volúmen de un cilindro \n 7.Realizar un algoritmo que lea el radio de una circunferencia y escriba la longitud de la misma y el área (pi*r)^2 del círculo inscrito. \n 8.Calcular el promedio de tres (3) números ingresados por teclado. \n 9.Devolver al menu anterior \n'))
    elif menuprincipal ==2:
        print ('Condicionales')
        condicionales=int(input('\n 1.Escribir un algoritmo para saber si el número ingresado por teclado es positivo o negativo. \n 2.Escribir un algoritmo que reciba dos números por teclado y diga cuál es el mayor y cuál el menor \n 3.Escriba un programa que lea tres números enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos. \n 4.Dados dos números A y B, sumarlos si A es menor que B o sino restarlos \n 5.Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por cero no está definida, en ese caso debe aparecer una leyenda anunciando que la división no es posible.\n 6.Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos.\n 7.Escribir un algoritmo que determine si un año es bisiesto o no. \n 8.Devolver al menu anterior \n'))
        while condicionales != 8:
            if condicionales ==1:
                print('Ingresar un numero y determinar si es positivo o negativo')
                numero=int(input('Escriba un numero:'))
                if numero < 0:
                   print('El numero',numero,'es negativo')
                else: 
                   print('El numero' ,numero, 'es positivo')       
                condicionales=int(input('\n 1.Escribir un algoritmo para saber si el número ingresado por teclado es positivo o negativo. \n 2.Escribir un algoritmo que reciba dos números por teclado y diga cuál es el mayor y cuál el menor \n 3.Escriba un programa que lea tres números enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos. \n 4.Dados dos números A y B, sumarlos si A es menor que B o sino restarlos \n 5.Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por cero no está definida, en ese caso debe aparecer una leyenda anunciando que la división no es posible.\n 6.Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos.\n 7.Escribir un algoritmo que determine si un año es bisiesto o no. \n 8.Devolver al menu anterior \n'))
            elif condicionales ==2:
                print('Ingresar dos numero y determinar cual es el mayor y cual es el menor')
                num1=int(input('Escriba el primer numero:'))
                num2=int(input('Escriba el segundo numero:'))
                if num1 < num2:
                    print('El numero mayor es',num2,'y el menor es',num1,)
                else: 
                    print('El numero mayor es',num1,'y el menor es',num2,)
                condicionales=int(input('\n 1.Escribir un algoritmo para saber si el número ingresado por teclado es positivo o negativo. \n 2.Escribir un algoritmo que reciba dos números por teclado y diga cuál es el mayor y cuál el menor \n 3.Escriba un programa que lea tres números enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos. \n 4.Dados dos números A y B, sumarlos si A es menor que B o sino restarlos \n 5.Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por cero no está definida, en ese caso debe aparecer una leyenda anunciando que la división no es posible.\n 6.Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos.\n 7.Escribir un algoritmo que determine si un año es bisiesto o no. \n 8.Devolver al menu anterior \n'))
            elif condicionales ==3:
                print('Ingresar tres numero y determinar cual es el mayor y cual es el menor')
                num1=int(input('Escriba el primer numero:'))
                num2=int(input('Escriba el segundo numero:'))
                num3=int(input('Escriba el tercer numero:'))
                mayor= num1
                if num2 > num1:
                    mayor= num2
                if num3 > num2:
                    mayor= num3
                elif num3 > num1:
                    mayor= num3
                    print('El numero mayor es:' , mayor)
                    menor= num1
                if num2 < num1:
                    menor= num2
                if num3 < num2:
                    menor= num3
                elif num3 < num1:
                    menor= num3
                    print('El numero menor es:' , menor)
                condicionales=int(input('\n 1.Escribir un algoritmo para saber si el número ingresado por teclado es positivo o negativo. \n 2.Escribir un algoritmo que reciba dos números por teclado y diga cuál es el mayor y cuál el menor \n 3.Escriba un programa que lea tres números enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos. \n 4.Dados dos números A y B, sumarlos si A es menor que B o sino restarlos \n 5.Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por cero no está definida, en ese caso debe aparecer una leyenda anunciando que la división no es posible.\n 6.Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos.\n 7.Escribir un algoritmo que determine si un año es bisiesto o no. \n 8.Devolver al menu anterior \n'))
            elif condicionales ==4:
                print('Dados dos números A y B, sumarlos si A es menor que B o sino restarlos')
                a=int(input('Escriba el primer numero:'))
                b=int(input('Escriba el segundo numero:'))
                suma=a+b
                resta=a-b
                if a < b:
                    print('El numero mayor es',b,)
                    print('El resultado de la suma es: ',suma)
                else:
                    print('El numero mayor es',a,)
                    print('El resultado de la resta es:', resta)
                condicionales=int(input('\n 1.Escribir un algoritmo para saber si el número ingresado por teclado es positivo o negativo. \n 2.Escribir un algoritmo que reciba dos números por teclado y diga cuál es el mayor y cuál el menor \n 3.Escriba un programa que lea tres números enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos. \n 4.Dados dos números A y B, sumarlos si A es menor que B o sino restarlos \n 5.Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por cero no está definida, en ese caso debe aparecer una leyenda anunciando que la división no es posible.\n 6.Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos.\n 7.Escribir un algoritmo que determine si un año es bisiesto o no. \n 8.Devolver al menu anterior \n'))
            elif condicionales ==5:
                    print('Dados dos números A y B encontrar el cociente entre A y B')
                    a=int(input('Escriba el primer numero:'))
                    b=int(input('Escriba el segundo numero:'))
                    if b == 0:
                        print('La division por 0 no es posible')
                    else:
                        cociente= a/b
                    print('El resultado de la division es:' , cociente)
                    condicionales=int(input('\n 1.Escribir un algoritmo para saber si el número ingresado por teclado es positivo o negativo. \n 2.Escribir un algoritmo que reciba dos números por teclado y diga cuál es el mayor y cuál el menor \n 3.Escriba un programa que lea tres números enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos. \n 4.Dados dos números A y B, sumarlos si A es menor que B o sino restarlos \n 5.Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por cero no está definida, en ese caso debe aparecer una leyenda anunciando que la división no es posible.\n 6.Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos.\n 7.Escribir un algoritmo que determine si un año es bisiesto o no. \n 8.Devolver al menu anterior \n'))
            elif condicionales ==6:
                    print('Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, si no multiplicar')
                    a=float(input('Escriba el primer numero:'))
                    b=float(input('Escriba el segundo numero:'))
                    suma=a+b
                    multiplicar=a*b
                    if a < 0 or b <0:
                        print('El resultado de la suma es: ',suma)
                    else:
                        print('El resultado de la multiplicacion es:', multiplicar)
                        condicionales=int(input('\n 1.Escribir un algoritmo para saber si el número ingresado por teclado es positivo o negativo. \n 2.Escribir un algoritmo que reciba dos números por teclado y diga cuál es el mayor y cuál el menor \n 3.Escriba un programa que lea tres números enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos. \n 4.Dados dos números A y B, sumarlos si A es menor que B o sino restarlos \n 5.Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por cero no está definida, en ese caso debe aparecer una leyenda anunciando que la división no es posible.\n 6.Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos.\n 7.Escribir un algoritmo que determine si un año es bisiesto o no. \n 8.Devolver al menu anterior \n'))
            elif condicionales ==7:
                    print ('Escribir un algoritmo que determine si un año es bisiesto o no')
                    year = int(input("Ingrese un año:\n"))
                    if year%100==0:
                        if year%400==0:
                            print(year, 'es bisiesto')
                        else:
 	                        print(year, 'no es bisiesto')
                    else:
                        if year%4==0:
 	                        print(year, 'es bisiesto')
                        else:
                            print(year, 'no es bisiesto')   
                    condicionales=int(input('\n 1.Escribir un algoritmo para saber si el número ingresado por teclado es positivo o negativo. \n 2.Escribir un algoritmo que reciba dos números por teclado y diga cuál es el mayor y cuál el menor \n 3.Escriba un programa que lea tres números enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos. \n 4.Dados dos números A y B, sumarlos si A es menor que B o sino restarlos \n 5.Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por cero no está definida, en ese caso debe aparecer una leyenda anunciando que la división no es posible.\n 6.Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos.\n 7.Escribir un algoritmo que determine si un año es bisiesto o no. \n 8.Devolver al menu anterior \n'))
            else:
                print('Digitaste una opcion incorrecta')
                condicionales=int(input('\n 1.Escribir un algoritmo para saber si el número ingresado por teclado es positivo o negativo. \n 2.Escribir un algoritmo que reciba dos números por teclado y diga cuál es el mayor y cuál el menor \n 3.Escriba un programa que lea tres números enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos. \n 4.Dados dos números A y B, sumarlos si A es menor que B o sino restarlos \n 5.Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por cero no está definida, en ese caso debe aparecer una leyenda anunciando que la división no es posible.\n 6.Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos.\n 7.Escribir un algoritmo que determine si un año es bisiesto o no. \n 8.Devolver al menu anterior \n'))
    elif menuprincipal ==3:
        print ('ciclos')
        ciclos=int(input('\n 1.Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2.Imprimir los números impares entre 0 y 100 \n 3.Imprimir los números pares del 1 al 100.\n 4.Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30. \n 5.Escribir un programa que sume los cuadrados de los cien primeros números naturales,mostrando el resultado en pantalla.\n 6.Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos losnúmeros comprendidos entre ellos en secuencia ascendente.\n 7.Sumar todos los números que se digitan por teclado mientras no sea cero. \n 8.Devolver al menu anterior \n'))
        while ciclos != 8:
            if ciclos ==1:
                print('Imprimir todos los múltiplos de 3 que hay entre 1 y 100')
                print('Los multiplos de 3 son:')
                for i in range(3, 100, 3):
                    print(i)        
                ciclos=int(input('\n 1.Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2.Imprimir los números impares entre 0 y 100 \n 3.Imprimir los números pares del 1 al 100.\n 4.Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30. \n 5.Escribir un programa que sume los cuadrados de los cien primeros números naturales,mostrando el resultado en pantalla.\n 6.Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos losnúmeros comprendidos entre ellos en secuencia ascendente.\n 7.Sumar todos los números que se digitan por teclado mientras no sea cero. \n 8.Devolver al menu anterior \n'))
            elif ciclos ==2:
                print('Imprimir los números impares entre 0 y 100.')
                print('Los numero impares son:')
                for i in range(1, 100, 2):
                    print(i) 
                ciclos=int(input('\n 1.Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2.Imprimir los números impares entre 0 y 100 \n 3.Imprimir los números pares del 1 al 100.\n 4.Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30. \n 5.Escribir un programa que sume los cuadrados de los cien primeros números naturales,mostrando el resultado en pantalla.\n 6.Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos losnúmeros comprendidos entre ellos en secuencia ascendente.\n 7.Sumar todos los números que se digitan por teclado mientras no sea cero. \n 8.Devolver al menu anterior \n'))
            elif ciclos ==3:
                print('Imprimir los números pares del 1 al 100')
                print('Los numero pares son:')
                for i in range(2, 101, 2):
                    print(i) 
                ciclos=int(input('\n 1.Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2.Imprimir los números impares entre 0 y 100 \n 3.Imprimir los números pares del 1 al 100.\n 4.Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30. \n 5.Escribir un programa que sume los cuadrados de los cien primeros números naturales,mostrando el resultado en pantalla.\n 6.Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos losnúmeros comprendidos entre ellos en secuencia ascendente.\n 7.Sumar todos los números que se digitan por teclado mientras no sea cero. \n 8.Devolver al menu anterior \n'))
            elif ciclos ==4:
                print('Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30')
                def Generar_cuadrados(n):
                    if 2 * n <= 30:
                        Cuadrados = [i ** 2 for i in range(1, 31)]
                        return Cuadrados[:n] + Cuadrados[-n:]
                resultado = Generar_cuadrados(15)
                print(resultado)
                ciclos=int(input('\n 1.Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2.Imprimir los números impares entre 0 y 100 \n 3.Imprimir los números pares del 1 al 100.\n 4.Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30. \n 5.Escribir un programa que sume los cuadrados de los cien primeros números naturales,mostrando el resultado en pantalla.\n 6.Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos losnúmeros comprendidos entre ellos en secuencia ascendente.\n 7.Sumar todos los números que se digitan por teclado mientras no sea cero. \n 8.Devolver al menu anterior \n'))
            elif ciclos ==5:
                print('Escribir un programa que sume los cuadrados de los cien primeros números naturales,mostrando el resultado en pantalla.')
                c=0
                s=0
                while (c<100):
                    c=c+1
                    s=s+c**2
                print("La suma de los cuadrados es: ",s)
                ciclos=int(input('\n 1.Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2.Imprimir los números impares entre 0 y 100 \n 3.Imprimir los números pares del 1 al 100.\n 4.Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30. \n 5.Escribir un programa que sume los cuadrados de los cien primeros números naturales,mostrando el resultado en pantalla.\n 6.Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos losnúmeros comprendidos entre ellos en secuencia ascendente.\n 7.Sumar todos los números que se digitan por teclado mientras no sea cero. \n 8.Devolver al menu anterior \n'))
            elif ciclos ==6:
                num1=int(input('Escriba un numero:'))
                num2=int(input('Escriba otro numero:'))
                if num2 > num1:
                    print(list(range(num1 +1, num2)))
                else:   
                    print('El primer numero digitado debe ser menor')        
                ciclos=int(input('\n 1.Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2.Imprimir los números impares entre 0 y 100 \n 3.Imprimir los números pares del 1 al 100.\n 4.Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30. \n 5.Escribir un programa que sume los cuadrados de los cien primeros números naturales,mostrando el resultado en pantalla.\n 6.Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos losnúmeros comprendidos entre ellos en secuencia ascendente.\n 7.Sumar todos los números que se digitan por teclado mientras no sea cero. \n 8.Devolver al menu anterior \n'))
            elif ciclos ==7:
                print('Sumar todos los números que se digitan por teclado mientras no sea cero')
                Sumar=0
                n=int(input("ingrese los numero a sumar(0 para finalizar): "))
                while n !=0:
                    if n > 0:
                        Sumar+= n
                        n=int(input("ingrese los numero a sumar(0 para finalizar): "))
                print('La suma de los numeros digitados es:' + str (Sumar))
                ciclos=int(input('\n 1.Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2.Imprimir los números impares entre 0 y 100 \n 3.Imprimir los números pares del 1 al 100.\n 4.Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30. \n 5.Escribir un programa que sume los cuadrados de los cien primeros números naturales,mostrando el resultado en pantalla.\n 6.Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos losnúmeros comprendidos entre ellos en secuencia ascendente.\n 7.Sumar todos los números que se digitan por teclado mientras no sea cero. \n 8.Devolver al menu anterior \n'))
            elif operadores ==8:
                ciclos=int(input('\n 1.Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2.Imprimir los números impares entre 0 y 100 \n 3.Imprimir los números pares del 1 al 100.\n 4.Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30. \n 5.Escribir un programa que sume los cuadrados de los cien primeros números naturales,mostrando el resultado en pantalla.\n 6.Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos losnúmeros comprendidos entre ellos en secuencia ascendente.\n 7.Sumar todos los números que se digitan por teclado mientras no sea cero. \n 8.Devolver al menu anterior \n'))
            else:
                print('Digitaste una opcion incorrecta')
                ciclos=int(input('\n 1.Imprimir todos los múltiplos de 3 que hay entre 1 y 100 \n 2.Imprimir los números impares entre 0 y 100 \n 3.Imprimir los números pares del 1 al 100.\n 4.Escribir un programa que imprima por pantalla los cuadrados de los números del 1 al 30. \n 5.Escribir un programa que sume los cuadrados de los cien primeros números naturales,mostrando el resultado en pantalla.\n 6.Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos losnúmeros comprendidos entre ellos en secuencia ascendente.\n 7.Sumar todos los números que se digitan por teclado mientras no sea cero. \n 8.Devolver al menu anterior \n'))
    else:
        print('Por favor digite la opcion correcta')       
    menuprincipal=int(input('Menu principal de miscelania: \n 1.Operadores \n 2.Condicionales \n 3.Ciclos \n 99.Salir \n'))
