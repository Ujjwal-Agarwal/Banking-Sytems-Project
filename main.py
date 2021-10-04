#TO include database model in c++, refer to https://www.notion.so/ujjwalagarwal/Database-Design-560d3ac728bc4661b638ede163025caa
#Start mysql server before running the program


import mysql.connector as mysql

#Initial SQL Server Connection
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
)

#Cursor Initialization
cursor = db.cursor()
#DAtabase creation if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS pydbtest")

#Second SQL connection to use the required database
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "pydbtest"
)

#Cursor initialized to use the current connection
cursor = db.cursor()

#DESCRIBE THE CUSTOMER TABLE
cursor.execute("CREATE TABLE IF NOT EXISTS CUSTOMER(CUSTOMER_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,CUSTOMER_NAME VARCHAR(20) NOT NULL,PHONE_NUMBER INT,EMAIL VARCHAR(50),DATE_OF_BIRTH DATE,USER_PASSWORD VARCHAR(64) NOT NULL,CUSTOMER_TYPE CHAR(3))")

#CREATE THE ACCOUNT TABLE
cursor.execute("CREATE TABLE IF NOT EXISTS ACCOUNT(ACCOUNT_ID VARCHAR(20) NOT NULL PRIMARY KEY,ACCOUNT_NAME VARCHAR(30) NOT NULL,DATE_OF_JOINING DATE,ACCOUNT_TYPE CHAR(3),CUSTOMER_ID INT NOT NULL, FOREIGN KEY(CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID) ON DELETE NO ACTION)")

#CREATE THE ACCOUNT_TYPE TABLE
cursor.execute("CREATE TABLE IF NOT EXISTS ACCOUNT_TYPE(ACCOUNT_TYPE CHAR(3), DESCRIPTION VARCHAR(100))")

#CREATE THE CUSTOMER_TYPE TABLE
cursor.execute("CREATE TABLE IF NOT EXISTS CUSTOMER_TYPE(CUSTOMER_TYPE CHAR(3), DESCRIPTION VARCHAR(100))")

#CREATE THE CUSTOMER TRANSACTION LOG
cursor.execute("CREATE TABLE IF NOT EXISTS CUSTOMER_TRANSACTION_LOG(CUSTOMER_TRANSACTION_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,DATE_OF_TRANSACTION DATE,TIME_OF_TRANSACTION VARCHAR(10),AMOUNT_MANIPULATED INT NOT NULL,BALANCE_BEFORE_TRANSACTION INT NOT NULL, BALANCE_AFTER_TRANSACTION INT NOT NULL,CUSTOMER_ID INT NOT NULL, FOREIGN KEY(CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID) ON DELETE NO ACTION)")

#CREATE THE BANKS TRANSACTION LOG
cursor.execute("CREATE TABLE IF NOT EXISTS BANK_TRANSACTION_LOG(TRANSACTION_ID VARCHAR(10) PRIMARY KEY,DATE_OF_TRANSACTION DATE,TIME_OF_TRANSACTION VARCHAR(10),AMOUNT_MANIPULATED INT,ACCOUNT_ID VARCHAR(20),CUSTOMER_TRANSACTION_ID INT,TRANSACTION_TYPE CHAR(5),FOREIGN KEY(ACCOUNT_ID) REFERENCES ACCOUNT(ACCOUNT_ID) ON DELETE NO ACTION,FOREIGN KEY(CUSTOMER_TRANSACTION_ID) REFERENCES CUSTOMER_TRANSACTION_LOG(CUSTOMER_TRANSACTION_ID))")

