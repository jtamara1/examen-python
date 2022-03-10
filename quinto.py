def porcentajes(redes,contabilidad,diseño):
    total = redes+contabilidad+diseño
    print(f"El porcentaje de redes es: {(redes/total)*100}%")
    print(f"El porcentaje de contabilidad es: {(contabilidad/total)*100}%")
    print(f"El porcentaje de diseño es: {(diseño/total)*100}%")
redes = int(input("Digite la cantidad de alumnos de redes\n"))
contabilidad = int(input("Digite la cantidad de alumnos de contabilidad\n"))
diseño = int(input("Digite la cantidad de alumnos de diseño\n"))
porcentajes(redes,contabilidad,diseño)