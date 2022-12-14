from random import randint
from time import sleep
import psycopg2
import csv
conexion=psycopg2.connect(user = 'siqrdvrm',password ='CBRDwebn0tVojx1sSOw_PhAvSsfOWw4_',host ='queenie.db.elephantsql.com',port= '5432',database = 'siqrdvrm')

def insertar(fecha,numganadorDia,numganadorNoche):
    cursor = conexion.cursor()
    sql = f'INSERT INTO loterias values(current_date,{numganadorDia},{numganadorNoche})'
    cursor.execute(sql)
    conexion.commit()

with open('Pick_3.csv') as h:
    reader=csv.reader(h)
    n = 1
    for row in reader:
        sleep(0.1)
        print(n,row[1],row[2])
        n=n+1
        insertar(f'{row[0]}',row[1],row[2])
#registro = cursor.fetchall()
#print(registro)
# def crearMatriz():
#     matrizIdentidad = []
#     num = 1
#     for r in range(999):
#         fila = []
#         for c in range(999):
#             fila.append(num)
#             num=num+1
        
#         matrizIdentidad.append(fila)


# crearMatriz()

