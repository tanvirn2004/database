# import mysql.connector
#
# connection = mysql.connector.connect(
#          host='127.0.0.1',
#          port= 3306,
#          database='flight_game',
#          user='root',
#          password='2004',
#          autocommit=True
#          )
#
# def get_airport_by_ident(idao):
#     sql =f"SELECT name, muncipality FROM airport WHERE ident='{idao}'"
#     print(sql)
#     cursor = connection.cursor(deictionary=True)
#     cursor.execute(sql)
#     result= cursor.fetchone()
#     print(result(['name'], result['muncipality']))
# code = input('Type Icao code:')
# get_airport_by_ident(co
# season = ('winter', 'spring', 'summer', 'autumn')
# month = int(input ('enter the month in number: '))
# if month in (1, 2 ,12):
#     print(f'It is {season[0]}')
# elif month in (3,4,5):
#     print(f'It is {season[1]}')
# elif month in (6,7,8):
#     print(f'It is {season[2]}')
#
# else:
#     print(f'it is {season[3]}')
import mysql.connector

connection = mysql.connector.connect(
          host='127.0.0.1',
          port= 3306,
          database='draft',
          user='root',
          password='2004',
          autocommit=True
         )

