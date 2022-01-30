CREATE TABLE EMPLOYEE (
	E_ID INT AUTO_INCREMENT PRIMARY KEY,
	E_Password VARCHAR(20),
	E_Name VARCHAR(20),
	E_Role VARCHAR(20),
	E_Phone BIGINT(10)
);

INSERT INTO EMPLOYEE (E_Name, E_Password, E_Role, E_Phone) VALUES('Fawaz Abid', '123', 'Manager', 8904751906);
INSERT INTO EMPLOYEE (E_Name, E_Password, E_Role, E_Phone) VALUES('Vinol Dsouza', '123','Manager', 8904751906);
INSERT INTO EMPLOYEE (E_Name, E_Password, E_Role, E_Phone) VALUES('Abhishek', '123', 'Delivery Staff', 8904751906);

-- ALTER TABLE ADD COLUMN E_Password VARCHAR(20);
-- UPDATE EMPLOYEE SET E_Password = '123';
-- ALTER TABLE EMPLOYEE MODIFY E_PHONE BIGINT(10)
-- SELECT * FROM EMPLOYEE;

CREATE TABLE SUPPLIER (
	S_ID INT AUTO_INCREMENT PRIMARY KEY,
	S_Name VARCHAR(30),
	S_Password VARCHAR(20),
	S_Phone BIGINT(10),
	S_Email VARCHAR(20),
	E_ID INT REFERENCES EMPLOYEE(E_ID) ON DELETE CASCADE
);

SELECT E_ID FROM EMPLOYEE WHERE E_ID = 1;

INSERT INTO SUPPLIER (S_Name, S_Password, S_Phone, S_Email, E_ID) VALUES('Abhishek Suppliers', '123', 8904751906, 'supplier@gmail.com', 1);
INSERT INTO SUPPLIER (S_Name, S_Password, S_Phone, S_Email, E_ID) VALUES('Vinol Suppliers', '123', 8904751906, 'supplier@gmail.com', 1);
INSERT INTO SUPPLIER (S_Name, S_Password, S_Phone, S_Email, E_ID) VALUES('Fawaz Suppliers', '123', 8904751906, 'supplier@gmail.com', 1);

-- SELECT * FROM SUPPLIER;

CREATE TABLE RETAILER (
	R_ID INT AUTO_INCREMENT PRIMARY KEY,
	R_Password VARCHAR(20),
	R_Name VARCHAR(30),
	R_Phone BIGINT(10),
	R_Email VARCHAR(20),
	R_Loc VARCHAR(20),
	E_ID INT REFERENCES EMPLOYEE(E_ID) ON DELETE CASCADE
);

INSERT INTO Retailer (R_Name, R_Password, R_Phone, R_Email, R_Loc, E_ID) VALUES('Fawaz Retailers', '123', 8904751906, 'retailer@gmail.com', 'Mangalore', 1);

-- SELECT * FROM RETAILER

CREATE TABLE ORDERS (
	O_ID INT AUTO_INCREMENT PRIMARY KEY,
	Ord_Date DATE,
	Rcv_Date DATE,
	S_ID INT REFERENCES SUPPLIER(S_ID) ON DELETE CASCADE,
	R_ID INT REFERENCES RETAILER(R_ID) ON DELETE CASCADE
);

CREATE TABLE ITEMS (
	I_ID INT AUTO_INCREMENT PRIMARY KEY,
	I_Name VARCHAR(20),
	Price FLOAT(10),
	Quantity INT(10),
	O_ID INT REFERENCES ORDERS(O_ID) ON DELETE CASCADE
);

-- ALTER TABLE EMPLOYEE ADD password varchar;

CREATE TABLE ITEMS_ORDERED (
	O_ID INT REFERENCES ORDERS(O_ID) ON DELETE CASCADE,
	I_ID INT REFERENCES ITEMS(I_ID) ON DELETE CASCADE,
	Quantity INT(10)
);

-- VIEW ORDERS
SELECT O.O_ID, O.Ord_Date, O.Rcv_Date, I.I_ID, I.I_Name, I.Price, I.Quantity
FROM ORDERS O, ITEMS I, ITEMS_ORDERED I_O
WHERE O.O_ID = I_O.O_ID AND I.I_ID = I_O.I_ID;

SELECT O.O_ID, O.Ord_Date, O.Rcv_Date FROM ORDERS

INSERT INTO `distributor`.`employee`
(`E_ID`,
`E_Name`,
`E_Role`,
`E_Phone`,
`password`)
VALUES
(2,
'vin',
'manager',
11212111,
'123123');
INSERT INTO `distributor`.`supplier`
(`S_ID`,
`S_Name`,
`S_Phone`,
`S_Email`,
`E_ID`)
VALUES
(1,
'FAW',
1111111,
'sdfsafd',
2);


INSERT INTO `distributor`.`retailer`
(`R_ID`,
`R_Name`,
`R_Phone`,
`R_Email`,
`Loc`,
`E_ID`)
VALUES
(3,
'abhi',
3231231,
'gfbdavd',
'dabradb',
2);










INSERT INTO `distributor`.`orders`
(`O_ID`,
`Cost`,
`Ord_date`,
`Rcv_date`,
`S_ID`,
`R_ID`)
VALUES
(1,
20,
'2022-01-01' ,
'2022-01-01',
1,
3);


INSERT INTO `distributor`.`items`
(
`I_Name`,
`Price`,
`Quantity`,
`O_ID`)
VALUES
(
'Faw',
50 ,
10 ,
1 );


INSERT INTO `distributor`.`orders`
(`O_ID`,

`Ord_date`,
`Rcv_date`,
`S_ID`
)
VALUES
(3,

curdate() ,
'2022-01-01',
1
);

INSERT INTO `ITEMS`
		( `I_Name`, `Price`, `Quantity`)
		VALUES
		( 'tom',  3, 5 );

UPDATE ITEMS
SET Quantity = 1000 + (SELECT Quantity FROM ITEMS WHERE I_ID = 6);
