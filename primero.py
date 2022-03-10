def distribucion(donacion):
    administracion = donacion*0.35
    sistemas = administracion*0.25
    telecomunicaciones = sistemas*0.1
    contabilidad = donacion - sistemas - administracion - telecomunicaciones
    print(f"El valor dado a a sistemas es: {sistemas}")
    print(f"El valor dado a administración es: {administracion}")
    print(f"El valor dado a telecomunicaciones es: {telecomunicaciones}")
    print(f"El valor dado a contabilidad es: {contabilidad}")

distribucion(float(input("Digite la candidad recibida en la donación\n")))