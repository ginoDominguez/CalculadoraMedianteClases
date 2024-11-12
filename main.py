## crear environment python -m venv venv
## activar: 

# main.py

from calculadora import Calculadora

calc = Calculadora()

while True:
    print("\nCalculadora Básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "5":
        print("¡Gracias por usar la calculadora!")
        break

    if opcion in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Por favor, ingresa números válidos.")
            continue

        if opcion == "1":
            print(f"Resultado: {calc.sumar(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado: {calc.restar(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado: {calc.multiplicar(num1, num2)}")
        elif opcion == "4":
            print(f"Resultado: {calc.dividir(num1, num2)}")
    else:
        print("Opción no válida. Intenta de nuevo.")