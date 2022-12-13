from random import randint
import psycopg2
import csv

with open(C:\Users\stive\Downloads)

conexion=psycopg2.connect(user = 'siqrdvrm',password ='CBRDwebn0tVojx1sSOw_PhAvSsfOWw4_',host ='queenie.db.elephantsql.com',port= '5432',database = 'siqrdvrm')

def insertar(fecha,numganadorDia,numganadorNoche):
    cursor = conexion.cursor()
    sql = f'INSERT INTO loterias values(current_date,{numganadorDia},{numganadorNoche})'
    cursor.execute(sql)
    conexion.commit()

insertar("2000",6000,7000)

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

