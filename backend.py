import os
from dotenv import load_dotenv
from mysql.connector import (connection)

load_dotenv()

# username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

def search_employee(name):
	
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"SELECT * FROM EMPLOYEE WHERE E_NAME = '{name}';")

	result = cur.fetchall()

	cnx.close()

	return result

print(search_employee('Vinol D Souza'))