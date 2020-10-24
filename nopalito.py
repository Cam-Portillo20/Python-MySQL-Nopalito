#Actividad No. 12 Nopalito
import mysql.connector

bd = mysql.connector.connect(user='cam',password='12345678',database='nopalito')

cursor = bd.cursor()

while True:
    print ('1) Agregar ubicacion')
    print ('2) Mostrar ubicaciones')
    print ('0) Salir')
    op = input()

    if op == '1':
        calle = input ('Calle: ')
        colonia = input ('Colonia: ')
        codigo_postal = input ('Codigo Postal: ')
        municipio = input ('Municipio: ')

        consulta = "INSERT INTO ubicacion(calle, colonia, codigo_postal, municipio) VALUES (%s, %s, %s, %s)"
        cursor.execute(consulta, (calle, colonia, codigo_postal, municipio))
        bd.commit()
        if cursor.rowcount:
            print ("Se agrego ubicacion")
        else:
            print("Error")
        
    elif op == '2':
        consulta = "SELECT * FROM ubicacion"

        cursor.execute(consulta)
        for row in cursor.fetchall():
            print("id: ",row[0])
            print("calle: ",row[1])
            print("colonia: ",row[2])
            print("codigo postal: ",row[3])
            print("municipio: ",row[4])
            
    elif op == '0':
        break
