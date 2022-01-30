import os
from dotenv import load_dotenv
from mysql.connector import (connection)

load_dotenv()

# username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

def add_new_item( order, item ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
		INSERT INTO `distributor`.`orders`
		( `Ord_date`, `Rcv_date`, `S_ID`)
		VALUES
		( curdate(), {order["rcv_date"]}, {order["s_id"]}); """)
	
	cur.execute(f"select MAX(O_ID) from orders")
	max_o_id = cur.fetchone()[0]
	
	cur.execute(f"""
		INSERT INTO `distributor`.`items`
		( `I_Name`, `Price`, `Quantity`, `O_ID`)
		VALUES
		( '{item["name"]}', {item["price"]} ,{item["quantity"]} ,{max_o_id} );""")

	cur.execute(f"select MAX(I_ID) from items")
	max_i_id = cur.fetchone()[0]

	cur.execute(f"""				
		INSERT INTO `distributor`.`items_ordered`
		( `O_ID`, `I_ID`, `Quantity` )
		VALUES
		( {max_o_id}, {max_i_id}, {item["quantity"]});""")

	cnx.commit()
	cnx.close()

# dummmy data

do = {
	"rcv_date": "04-03-01",
	"s_id": 2
}

di = {
	"name": "tomato",
	"price": 20,
	"quantity": 100
}

add_new_item(do, di)

def add_orders(rcv_date,S_ID,lst_items ):
	
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
		INSERT INTO `distributor`.`orders`
		( `Ord_date`, `Rcv_date`, `S_ID`)
		VALUES
		( curdate(), {rcv_date}, {S_ID}); """)
	
	cur.execute(f"select MAX(O_ID) from orders")
	max_o_id=cur.fetchone()

	for i in lst_items:
		cur.execute(f"""
			INSERT INTO `distributor`.`items`
			( `I_Name`, `Price`, `Quantity`, `O_ID`)
			VALUES
			( {i.name}, {i.price} ,{i.quantity} ,{max_o_id} );""")

		cur.execute(f"select MAX(I_ID) from items")
		max_i_id=cur.fetchone()

		cur.execute(f"""				
			INSERT INTO `distributor`.`items_ordered`
			( `I_ID`, `O_ID`, `Quantity` )
			VALUES
			( {max_i_id}, {max_o_id}, {i.quantity}, {max_o_id} );""")

	result = cur.fetchall()
	cnx.close()

	return result

# print(add_orders('Vinol D Souza'))

def add_new_employee( eid,ename, role,ephone,epass ):
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""
		INSERT INTO `distributor`.`employee`
		(`E_ID`,`E_Name`,`E_Role`,`E_Phone`,`password`)
		VALUES
		({eid},{ename},{role},{ephone},{epass}); """)
	
	

	cnx.commit()
	cnx.close()

	# add_new_employee('3','willy','manager',1112313,'willy123')

def add_new_supplier( sname,sphone,semail ):
		cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
		cur = cnx.cursor()

		cur.execute(f"""
			INSERT INTO `distributor`.`supplier`
			(`S_Name`,`S_Email`,`S_Phone`)
			VALUES
			({sname},{sphone},{semail}); """) 

			# not sure how to get emp_id in here

		cnx.commit()
		cnx.close()

	

def add_new_retailer( rname,rphone,remail,rloc ):
		cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
		cur = cnx.cursor()

		cur.execute(f"""git
			INSERT INTO `distributor`.`retailer`
			(`R_Name`,`R_Phone`,`R_Email`,`Loc`)
			VALUES
			({rname},{rphone},{remail},{rloc}); """) 

			# not sure how to get emp_id in here

		cnx.commit()
		cnx.close()
