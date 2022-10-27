import csv
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
i=0
a="example";
f=".csv";
Datosespacio = {}
Datosespaciob = {}
fechadia =(datetime.today().strftime('%Y-%m-%d'))
fechames= (datetime.today().strftime('%m'))
WESPACIO = ""

print(fechadia)
print("Hola "+fechames)
with open('bwq.csv', "r") as archivo:
    # Omitir el encabezado
    next(archivo, None)
    for linea in archivo:
        # Remover salto de línea
        linea = linea.rstrip()
        # Ahora convertimos la línea a arreglo con split
        separador = ","
        lista = linea.split(",")
        # Tenemos la lista. En la 0 tenemos el nombre, en la 1 la calificación y en la 2 el precio
        espacio = lista[0]
        espacio = espacio.replace('"', '')
        xfecha = lista[1]
        xData = lista[2]
        xData = xData[2:6]

        xfecha = xfecha[1:11]
        ddfecha = xfecha[6:8]

        if ddfecha == fechames:

            if xData == "Alto":

            #valida si se registro para el mes el espacio

                Datosespacio[espacio] = "Alta"

            # si no exite se registra
            else :
                if xData == "Baja":
                    Datosespaciob[espacio] = "Baja"
        else :
            print("Salio")




        name = a + str(i) + f;
        print(name)



         #   print("Writing complete")



        myData =Datosespaciob
        archi1 = open("datos.txt", "w")
        archi1.write('Reporte de espacios conocupacion Alta y baja ')
        archi1.write("\n")
        archi1.write(fechadia)
        archi1.write("\n")
        archi1.write("Espacios con ocupacion alta")
        archi1.write("\n")
        archi1.write(str(Datosespacio))
        archi1.write("\n")
        archi1.write("Espacios con ocupacion Baja")
        archi1.write("\n")
        archi1.write(str(Datosespaciob))
        archi1.write("\n")
        archi1.write("----fIN----")
        archi1.close()

        print("Writing complete")
