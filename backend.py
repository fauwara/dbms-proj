import os
from dotenv import load_dotenv
from mysql.connector import (connection)

load_dotenv()

# username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

########################################################### ADD NEW ITEM ##################################################################

def add_new_item( order, item ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
		INSERT INTO ORDERS
		( Ord_date, Rcv_Date, S_ID )
		VALUES
		( curdate(), '{order["rcv_date"]}', '{order["s_id"]}' ); """)
	
	cur.execute(f"select MAX(O_ID) from orders;")
	max_o_id = cur.fetchone()[0]
	
	cur.execute(f"""
		INSERT INTO ITEMS
		( I_Name, Price, Quantity )
		VALUES
		( '{item["name"]}', {item["price"]} ,{item["quantity"]} );""")

	cur.execute(f"select MAX(I_ID) from items;")
	max_i_id = cur.fetchone()[0]

	cur.execute(f"""
		INSERT INTO ITEMS_ORDERED
		( O_ID, I_ID, Quantity )
		VALUES
		( {max_o_id}, {max_i_id}, {item["quantity"]}); """)

	cnx.commit()
	cnx.close()

# dummmy data

# do = {
# 	"rcv_date": "2022-02-10", #YYYYMMDD
# 	"s_id": 1
# }

# di = {
# 	"name": "potato",
# 	"price": 20,
# 	"quantity": 100
# }

# add_new_item(do, di)

########################################################### UPDATE STOCK ###################################################################

def update_stock( order, items ):
	
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
		INSERT INTO ORDERS
		( Ord_date, Rcv_Date, S_ID )
		VALUES
		( curdate(), '{order["rcv_date"]}', {order["s_id"]} ); """)
	
	cur.execute(f"select MAX(O_ID) from orders")
	max_o_id = cur.fetchone()[0]

	for i in items:
		cur.execute(f"SELECT Quantity FROM ITEMS WHERE I_ID = {i['id']} ")
		item_quantity = cur.fetchone()[0] + i['quantity']

		cur.execute(f" UPDATE ITEMS SET Quantity = {item_quantity} WHERE I_ID = {i['id']}; ")

		cur.execute(f"""
			INSERT INTO ITEMS_ORDERED
			( O_ID, I_ID, Quantity )
			VALUES
			( {max_o_id}, {i['id']}, {i['quantity']});""")

	cnx.commit()
	cnx.close()

# def update_stock( order, items ):
	
# 	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
# 	cur = cnx.cursor()

# 	if ['role']
# 	cur.execute(f"""
# 		INSERT INTO ORDERS
# 		( Ord_date, Rcv_Date, S_ID )
# 		VALUES
# 		( curdate(), '{order["rcv_date"]}', {order["s_id"]} ); """)
	
# 	cur.execute(f"select MAX(O_ID) from orders")
# 	max_o_id = cur.fetchone()[0]

# 	for i in items:
# 		cur.execute(f"SELECT Quantity FROM ITEMS WHERE I_ID = {i['id']} ")
# 		item_quantity = cur.fetchone()[0] + i['quantity']

# 		cur.execute(f" UPDATE ITEMS SET Quantity = {item_quantity} WHERE I_ID = {i['id']}; ")

# 		cur.execute(f"""
# 			INSERT INTO ITEMS_ORDERED
# 			( O_ID, I_ID, Quantity )
# 			VALUES
# 			( {max_o_id}, {i['id']}, {i['quantity']});""")

# 	cnx.commit()
# 	cnx.close()


# dummy data

# order = {
# 	"rcv_date": "2022-02-10",
# 	"s_id": 1
# }

# items = [
# 	{
# 		"id": "7",
# 		"quantity": 100
# 	},
# 	{
# 		"id": "10",
# 		"quantity": 200
# 	},
# ]

# items = [
# 	{
# 		"id": "7",
# 		"quantity": 100
# 	},
# 	{
# 		"id": "10",
# 		"quantity": 200
# 	},
# ]

# update( order, items )

########################################################### VIEWING ORDERS ###################################################################

def get_orders():
	
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
		SELECT O.O_ID, O.Ord_Date, O.Rcv_Date, I.I_ID, I.I_Name, I.Price, I.Quantity
		FROM ORDERS O, ITEMS I, ITEMS_ORDERED I_O
		WHERE O.O_ID = I_O.O_ID AND I.I_ID = I_O.I_ID;
	""")
	
	result = cur.fetchall()
	
	cnx.commit()
	cnx.close()

	return result

########################################################### VIEWING ITEMS ###################################################################

def get_items():
	
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f""" SELECT I_Name, Price, Quantity FROM ITEMS """)
	
	result = cur.fetchall()
	
	cnx.commit()
	cnx.close()

	return result

# for i in get_items():
# 	print(i)

########################################################### ADD EMPLOYEE ###################################################################

def add_new_employee( eid, epass, ename, role, ephone ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
		INSERT INTO EMPLOYEE
		( E_ID, E_Password, E_Name, E_Role, E_Phone, )
		VALUES
		( {eid}, {epass}, {ename}, {role}, {ephone} ); """)
	
	cnx.commit()
	cnx.close()



# add_new_employee('3', 'willy123', 'willy','delivery man', 1112313)

########################################################### ADD SUPPLIER ###################################################################

def add_new_supplier( user_data ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	try:
		cur.execute(f"""
			INSERT INTO SUPPLIER
			( S_ID, S_Password, S_Name, S_Email, S_Phone, E_ID )
			VALUES
			('{user_data['username']}', '{user_data['password']}', '{user_data['name']}', '{user_data['email']}', {user_data['phone']}, 'fauwara');""") 
	
		cnx.commit()
		cnx.close()
		
		return 1

	except :
		cnx.close()
		return 0

########################################################### ADD RETAILER ###################################################################

def add_new_retailer( user_data ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	try:
		cur.execute(f"""
			INSERT INTO RETAILER
			( R_ID, R_Password, R_Name, R_Email, R_Phone, E_ID )
			VALUES
			('{user_data['username']}', '{user_data['password']}', '{user_data['name']}', '{user_data['email']}', {user_data['phone']}, 'fauwara');""") 
	
		cnx.commit()
		cnx.close()
		
		return 1

	except :
		cnx.close()
		return 0

############################################################# LOGIN  ###################################################################

def login_supplier(user_data):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()
	
	cur.execute(f"""
		SELECT S_Password FROM SUPPLIER 
		WHERE S_ID = '{user_data['username']}'
		""")
	
	user_pass = cur.fetchone()
	if user_pass:
		if user_pass[0] == user_data['password']:
			return 1
		else:
			return 0
	else:
		return 0

def login_retailer(user_data):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
		SELECT R_Password FROM RETAILER 
		WHERE R_ID = '{user_data['username']}'
	""")

	user_pass = cur.fetchone()
	if user_pass:
		if user_pass[0] == user_data['password']:
			return 1
		else:
			return 0
	else:
		return 0

def login_employee(user_data):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
		SELECT E_Password FROM EMPLOYEE 
		WHERE E_ID = '{user_data['username']}'
		""")

	user_pass = cur.fetchone()
	if user_pass:
		if user_pass[0] == user_data['password']:
			return 1
		else:
			return 0
	else:
		return 0

########################################################### SALES OF TODAY ###################################################################

def sales_of_today():
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
		SELECT O.O_ID, O.Ord_Date, O.Rcv_Date, I.I_ID, I.I_Name, I.Price, I.Quantity
		FROM ORDERS O, ITEMS I, ITEMS_ORDERED I_O
		WHERE O.O_ID = I_O.O_ID AND I.I_ID = I_O.I_ID AND O.Ord_Date = CURDATE();
	""")
	
	result = cur.fetchall()
	
	cnx.commit()
	cnx.close()

	return(result)

# for i in sales_of_today():
# 	print(i)

########################################################### GET-DETAILS ###################################################################

def get_sup( sid ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
	SELECT * FROM SUPPLIER
	WHERE S_ID={sid}
	 """) 

	result = cur.fetchone()	

	cnx.commit()
	cnx.close()

	return result


def get_emp( eid ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
	SELECT * FROM EMPLOYEE
	WHERE E_ID={eid}
	 """) 

	result = cur.fetchone()	

	cnx.commit()
	cnx.close()

	return result

def get_ret( rid ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
	SELECT * FROM SUPPLIER
	WHERE R_ID={rid}
	 """) 

	result = cur.fetchone()	

	cnx.commit()
	cnx.close()

	return result