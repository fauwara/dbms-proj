import os
from dotenv import load_dotenv
from mysql.connector import (connection)

load_dotenv()

# username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

def add_orders(rcv_date,S_ID,lst_items):
	
	cnx = connection.MySQLConnection( user='root', password=password, host='127.0.0.1', database='distributor' )
	cur = cnx.cursor()

	cur.execute(f"""				
						INSERT INTO `distributor`.`orders`
						(
						`Ord_date`,
						`Rcv_date`,
						`S_ID`
						)
						VALUES
						(
						curdate() ,
						{rcv_date},
						{S_ID}
						);""")
	cur.execute(f"select MAX(O_ID) from orders")
	max_o_id=cur.fetchone()

	for i in lst_items:

		cur.execute(f"""				
							INSERT INTO `distributor`.`items`
							(
							`I_Name`,
							`Price`,
							`Quantity`,
							`O_ID`)
							VALUES
							(
							{i.name},
							{i.price} ,
							{i.quantity} ,
							{max_o_id} );""")

		cur.execute(f"select MAX(I_ID) from items")
		max_i_id=cur.fetchone()

		cur.execute(f"""				
							INSERT INTO `distributor`.`items_ordered`
							(
							`I_ID`,
							`O_ID`,
							`Quantity`
							)
							VALUES
							(
							{max_i_id},
							{max_o_id} ,
							{i.quantity} ,
							{max_o_id} );""")

	result = cur.fetchall()

	cnx.close()

	return result

print(add_orders('Vinol D Souza'))