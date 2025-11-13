from funtions import suma
from calculo import calcula_area_cU, calcul_area_t, c_area_circu

print("practica_131125")
def mostrar_menu():
    
    
    print("-----menu-----")
    print("1 para calcular el area de triangulo")
    print("2 para calcular el area del cuadrado")
    print("3 para sumar")
    print("4 para calcular el radio de un circulo")
    print("5 para salir")

while True:
    mostrar_menu()
    opcion=input("selecciona la opcion:")

    if opcion == "1" :
        
        base= float(input("digite una base:"))
        altura=float(input("digite una altura:"))
        area1= calcul_area_t(base, altura)
        print(f"el area del traingulo es: {area1}")


    elif opcion == "2" :

        lado=float(input("digite un lado:"))    
        area2= calcula_area_cU (lado)
        print(f"el area del cuadrado es: {area2}")

    elif opcion == "3":

        num1= float (input("digite un numero:"))
        num2 =float (input("digite un numero:"))
        resultado = suma (num1, num2) 
        print(f"la suma es: {resultado}")

    elif opcion =="4":

        radio=float (input("digite un numero"))
        area3= c_area_circu(radio)
        print(f"el radio es: {area3}")

    elif opcion == "5" :

        print("hasta pronto!")
        break
    else:
        print("opcion invalida, intente de nuevo")

