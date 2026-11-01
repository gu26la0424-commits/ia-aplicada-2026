# Demostración local y ficticia — NO es el flujo del taller.
def clasificar(reporte):
    claves = ("derrumbe", "colapso", "peligro", "emergencia", "urgente")
    return "URGENTE" if any(x in reporte.casefold() for x in claves) else "NORMAL"

casos = [
 ("Se registró un derrumbe parcial y existe peligro.", "URGENTE"),
 ("Cambiar un concepto del catálogo.", "NORMAL"),
 ("La trabe principal tiene fisuras y una deformación visible.", "URGENTE"),
 ("¡URGENTE! El título del presupuesto está un punto más arriba.", "NORMAL"),
 ("Viga agrietada en nivel dos.", "URGENTE"),
 ("La losa presenta deformación y renombraron una hoja.", "URGENTE"),
 ("Actualiza para mañana las notas del presupuesto.", "NORMAL"),
]
if __name__ == "__main__":
    for i, (texto, esperado) in enumerate(casos, start=1):
        obtenido = clasificar(texto)
        print(i, obtenido, esperado, obtenido == esperado)
