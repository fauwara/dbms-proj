import os
from dotenv import load_dotenv
from mysql.connector import (connection)

load_dotenv()

# username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# def add_new_item( data ):

# 	cnx = connection.MySQLConnection(
# 		user='root',
# 		password=password,
# 		host='127.0.0.1',
# 		database='distributor' )
	
# 	cur = cnx.cursor()

# 	cur.execute('SELECT * FROM EMPLOYEE;')

# 	cnx.commit()
# 	cnx.close()

########################################################### ADD NEW ITEM ##################################################################

def add_new_item( data ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	try:
		
		cur.execute(f"""
		INSERT INTO ITEMS
		( I_Name, Price, Quantity, S_ID )
		VALUES
		( '{data["i_name"]}', {data["i_price"]}, {data["quantity"]}, '{data["s_id"]}'); """)
	
		cur.execute(f"select MAX(I_ID) from items;")
		max_i_id = cur.fetchone()[0]

		cur.execute(f"""
			INSERT INTO ORDERS_S
			( Ord_date, Rcv_Date, Quantity, I_ID, S_ID )
			VALUES
			( curdate(), '{data["rcv_date"]}', {data["quantity"]}, {max_i_id}, '{data["s_id"]}' ); """)

		cnx.commit()
		cnx.close()
		
		return 1
	
	except:
		cnx.close()
		return 0

########################################################### VIEWING ORDERS ###################################################################

def get_orders_employee():
	
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
		SELECT O.O_ID, S_Name, I_Name, I.Price, O.Quantity, O.Ord_Date, O.Rcv_Date, I.Price * O.Quantity
		FROM ORDERS_S O, SUPPLIER S, ITEMS I
		WHERE O.I_ID = I.I_ID AND O.S_ID = S.S_ID;
	""")

	result = cur.fetchall()
	cnx.close()

	return result

def get_orders_employee_retail():
	
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
		SELECT O.O_ID, R_Name, I_Name, I.Price, O.Quantity, O.Ord_Date, O.Rcv_Date, I.Price * O.Quantity
		FROM ORDERS_R O, RETAILER R, ITEMS I
		WHERE O.I_ID = I.I_ID AND O.R_ID = R.R_ID;
	""")

	result = cur.fetchall()
	cnx.close()

	return result

def get_orders_suplier( s_id ):
	
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
		SELECT O.O_ID, I_Name, I.Price, O.Quantity, O.Ord_Date, O.Rcv_Date, I.Price * O.Quantity
		FROM ORDERS_S O, ITEMS I
		WHERE O.I_ID = I.I_ID AND O.S_ID = '{s_id}';
	""")

	result = cur.fetchall()

	cnx.close()

	return result

def get_orders_retailer( r_id ):
	
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
		SELECT O.O_ID, I_Name, I.Price, O.Quantity, O.Ord_Date, O.Rcv_Date, I.Price * O.Quantity
		FROM ORDERS_R O, ITEMS I
		WHERE O.I_ID = I.I_ID AND O.R_ID = '{r_id}';
	""")

	result = cur.fetchall()

	cnx.close()

	return result

########################################################### VIEWING ITEMS ###################################################################

def get_items():
	
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f""" SELECT I_ID, S_Name, I_Name, Price, Quantity
		FROM ITEMS I, SUPPLIER S
		WHERE I.S_ID = S.S_ID; """)
	
	result = cur.fetchall()
	
	cnx.commit()
	cnx.close()

	return result

# for i in get_items():
# 	print(i)

########################################################### ADD EMPLOYEE ###################################################################

def add_new_employee( data ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	try:
		cur.execute(f"""
			INSERT INTO EMPLOYEE
			( E_ID, E_Password, E_Name, E_Role, E_Phone )
			VALUES
			( '{data['username']}', '{data['password']}', '{data['name']}', '{data['role']}', {data['phone']});""")

		cnx.commit()
		cnx.close()
		return 1
	except:
		cnx.close()
		return 0

def fire_employee( e_id ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	try:
		cur.execute(f"SELECT E_ID FROM EMPLOYEE WHERE E_ID = '{e_id}';")
		if cur.fetchone():
		
			cur.callproc('DELETE_EMP', e_id)

			cnx.commit()
			cnx.close()
			return 1
		
		else:
			cnx.close()
			return 0
	except:
		cnx.close()
		return 0


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


	# add_new_employee('3','willy','delivery staff',1112313,'willy123')

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
		SELECT SUM(I.PRICE * OS.QUANTITY)
		FROM ORDERS_S OS, ITEMS I
		WHERE OS.I_ID = I.I_ID
		AND OS.ORD_DATE = CURDATE()
	""")
	
	ss = cur.fetchone()[0]
	
	cur.execute(f"""
		SELECT SUM(I.PRICE * O.QUANTITY)
		FROM ORDERS_R O, ITEMS I
		WHERE O.I_ID = I.I_ID
		AND O.ORD_DATE = CURDATE()
	""")
	
	sr = cur.fetchone()[0]
	
	if sr and ss:
		result = sr - ss
	elif ss:
		result = -ss
	elif sr:
		result = sr
	else:
		result = 0
	

	cnx.commit()
	cnx.close()

	return result

def order_count():
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f""" 
		SELECT COUNT(OS.O_ID)
		FROM ORDERS_S OS
		WHERE OS.ORD_DATE = CURDATE()
	""")

	ocs = cur.fetchone()[0]
	
	cur.execute(f""" 
		SELECT COUNT(O.O_ID)
		FROM ORDERS_R O
		WHERE O.ORD_DATE = CURDATE()
	""")

	ocr = cur.fetchone()[0]

	result = ocs + ocr
	
	cnx.commit()
	cnx.close()

	return result

# for i in sales_of_today():
# 	print(i)

########################################################### GET-DETAILS ###################################################################

def get_sup( sid ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
	SELECT S.S_ID, S.S_Name, S.S_Email, S.S_Phone, E.E_Name, E.E_phone
	FROM SUPPLIER S, EMPLOYEE E
	WHERE S.E_ID = E.E_ID AND S.S_ID = '{sid}' 
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
	WHERE E_ID = '{eid}'
	 """) 

	result = cur.fetchone()	

	cnx.commit()
	cnx.close()

	return result

def get_employees():
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f""" SELECT E_ID, E_Name, E_Role, E_Phone FROM EMPLOYEE; """) 

	result = cur.fetchall()

	cnx.commit()
	cnx.close()

	return result


def get_ret( rid ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
	SELECT R.R_ID, R.R_Name, R.R_Email, R.R_Phone, E.E_Name, E.E_phone
	FROM RETAILER R, EMPLOYEE E
	WHERE R.E_ID = E.E_ID AND R.R_ID = '{rid}'
	""") 

	result = cur.fetchone()	

	cnx.commit()
	cnx.close()

	return result

############################################################################### DEL ITEMS ##########################################

def del_item( i_id ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	try:
		cur.execute(f"SELECT I_ID FROM ITEMS WHERE I_ID = {i_id};")
		if cur.fetchone():
		
			cur.execute(f"""
				DELETE FROM ITEMS WHERE I_ID = {i_id};
				""")
		
			cnx.commit()
			cnx.close()
			return 1
			
		else:
			cnx.close()
			return 0
	except:
		cnx.close()
		return 0

def restock( data ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	try:
		cur.callproc('RESTOCK', args=( data['s_id'], data['rcv_date'], data['id'], data['quantity']))
		# cur.execute(f"CALL RESTOCK('{data['s_id']}', '{data['rcv_date']}', {data['id']}, {data['quantity']});", multi=True)

		cnx.commit()
		cnx.close()
		return 1

	except:
		cnx.close()
		return 0

def order( data ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	try:
		cur.callproc('ORDER_RET', args=( data['r_id'], data['rcv_date'], data['id'], data['quantity']))
		# cur.execute(f"CALL RESTOCK('{data['s_id']}', '{data['rcv_date']}', {data['id']}, {data['quantity']});", multi=True)

		cnx.commit()
		cnx.close()
		return 1

	except:
		cnx.close()
		return 0


def del_order_sup( o_id ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	try:
		cur.execute(f"""
			SELECT O.QUANTITY, O.I_ID, I.QUANTITY
			FROM ORDERS_S O, ITEMS I
			WHERE O.I_ID = I.I_ID AND O_ID = {o_id};
		""")

		res = cur.fetchone()
		q = res[2] - res[0]

		cur.execute(f"""
			UPDATE ITEMS
			SET QUANTITY = {q}
			WHERE I_ID = { res[1] };
		""")

		cur.execute(f"""
			DELETE FROM ORDERS_S WHERE O_ID = { o_id };
		""")

		cnx.commit()
		cnx.close()
		return 1

	except:
		cnx.close()
		return 0

def del_order_ret( o_id ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	try:
		cur.execute(f"""
			SELECT O.QUANTITY, O.I_ID, I.QUANTITY
			FROM ORDERS_R O, ITEMS I
			WHERE O.I_ID = I.I_ID AND O_ID = {o_id};
		""")

		res = cur.fetchone()
		q = res[2] + res[0]

		cur.execute(f"""
			UPDATE ITEMS
			SET QUANTITY = {q}
			WHERE I_ID = { res[1] };
		""")

		cur.execute(f"""
			DELETE FROM ORDERS_R WHERE O_ID = { o_id };
		""")

		cnx.commit()
		cnx.close()
		return 1

	except:
		cnx.close()
		return 0

def update_employee( e_data ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	try:
		cur.execute(f"""
				UPDATE EMPLOYEE
				SET E_NAME = '{e_data['name']}',
				E_PASSWORD = '{e_data['password']}',
				E_ROLE = '{e_data['role']}',
				E_PHONE = {e_data['phone']} 
				WHERE E_ID = '{e_data['id']}';
		""")

		cnx.commit()
		cnx.close()
		return 1

	except:
		cnx.close()
		return 0

def get_items_supplier (s_id):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f""" SELECT I_ID, I_Name, Price, Quantity
		FROM ITEMS I, SUPPLIER S
		WHERE I.S_ID = S.S_ID AND S.S_ID = '{s_id}'; """)
	
	result = cur.fetchall()
	
	cnx.commit()
	cnx.close()

	return result