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

# do = {
# 	"rcv_date": "04-03-01",
# 	"s_id": 2
# }

# di = {
# 	"name": "tomato",
# 	"price": 20,
# 	"quantity": 100
# }

# add_new_item(do, di)

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