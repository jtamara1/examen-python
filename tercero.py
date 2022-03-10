def vendedor(base,ventas):
    comision = ventas*0.15
    print(f"La comisión ganada por el vendedor es: {comision}")
    print(f"El total a pagar al vendedor es: {base+comision}")

base = float(input("Digite el salario base del vendedor\n"))
ventas = float(input("Digite la cantidad de ventas del vendedor\n"))
vendedor(base,ventas)