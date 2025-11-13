from funtions import suma
from calculo import calcular_area_cU, calcular_area_t

def mostrar_menu():
    
    print("-----menu-----")
    print("1 para calcular el area de triangulo")
    print("2 para calcular el area del cuadrado")
    print("3 para sumar")
    print("4 para salir")

while True:
    mostrar_menu()
    opcion=input("selecciona la opcion:")

    if opcion == "1" :
        
        base= float(input("digite una base:"))
        altura=float(input("digite una altura:"))
        area1= calcular_area_t(base, altura)
        print(f"el area del traingulo es: {area1}")


    elif opcion == "2" :

        lado=float(input("digite un lado:"))    
        area2= calcular_area_cU (lado)
        print(f"el area del cuadrado es: {area2}")

    elif opcion == "3":

        num1= float (input("digite un numero:"))
        num2 =float (input("digite un numero:"))
        resultado = suma (num1, num2) 
        print(f"la suma es: {resultado}")

    elif opcion == "4" :

        print("hasta pronto!")
        break
    else:
        print("opcion invalida, intente de nuevo")

