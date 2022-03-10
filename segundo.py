def porcentajes_inversion(primera,segunda,tercera):
    total = primera+segunda+tercera
    print(f"El porcentaje de la primera persona es {(primera/total)*100}%")
    print(f"El porcentaje de la segunda persona es {(segunda/total)*100}%")
    print(f"El porcentaje de la tercera persona es {(tercera/total)*100}%")

primera = float(input("Digite la inversión de la primera persona\n"))
segunda = float(input("Digite la inversión de la segunda persona\n"))
tercera = float(input("Digite la inversión de la tercera persona\n"))
porcentajes_inversion(primera,segunda,tercera)