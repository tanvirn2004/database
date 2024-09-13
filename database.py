import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='people',
         user='kwargs',
         password='2004',
         autocommit=True
         )

def get_airport_by_ident(idao):
    sql =f"SELECT name, muncipality FROM airport WHERE ident='{idao}'"
    print(sql)
    cursor = connection.cursor(deictionary=True)
    cursor.execute(sql)
    result= cursor.fetchone()
    print(result(['name'], result['muncipality']))
code = input('Type Icao code:')
get_airport_by_ident(code)