def definitiva(taller1,taller2,taller3,examen,proyecto):
    definitiva = (((taller1+taller2+taller3)/3)*0.5)+(examen*0.3)+(proyecto*0.2)
    print(f"Su nota definitiva es: {definitiva}")
taller1 = float(input("Digite la nota del taller 1\n"))
taller2 = float(input("Digite la nota del taller 2\n"))
taller3 = float(input("Digite la nota del taller 3\n"))
examen = float(input("Digite la nota del examen en clase\n"))
proyecto = float(input("Digite la nota del proyecto final\n"))
definitiva(taller1,taller2,taller3,examen,proyecto)