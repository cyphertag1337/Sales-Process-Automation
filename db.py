# imports
import sqlite3

#====================================================TABLES===========================================================================================================================

def createLeadTable():
    con = sqlite3.connect("sales.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Leads(LEAD_ID INTEGER PRIMARY KEY, NAME VARCHAR(50), EMAIL VARCHAR(20), PHONE_NO NUMBER(10), DESCRIPTION LONGTEXT, IS_CONVERTED BOOLEAN)")
    con.commit()
    con.close()
    
def createCustomerTable():
    con = sqlite3.connect("sales.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Customers(ID INTEGER PRIMARY KEY, NAME TEXT, EMAIL VARCHAR(20), PHONE_NO NUMBER(10))")
    cur.execute(
        '''
        CREATE TRIGGER IF NOT EXISTS convert_lead AFTER UPDATE ON Leads
        BEGIN
            INSERT INTO Customers VALUES (NULL, new.NAME, new.EMAIL, new.PHONE_NO);
        END;
        '''
    )
    con.commit()
    con.close()
    
def createOrderTable():
    con = sqlite3.connect("sales.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Orders(ORDER_NO INTEGER PRIMARY KEY, CUST_ID INTEGER, SUBTOTAL DECIMAL(10,2), DISCOUNT DECIMAL(10,2), GRAND_TOTAL DECIMAL(10,2))")
    con.commit() 
    con.close()
    
    
#======================================================FUNCTIONS=========================================================================================================================

def addLeadData(NAME='', EMAIL='', PHONE_NO='', DESCRIPTION='', IS_CONVERTED=False):
    con = sqlite3.connect("sales.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Leads VALUES(NULL, ?,?,?,?,?)", (NAME, EMAIL, PHONE_NO, DESCRIPTION, IS_CONVERTED))
    con.commit()
    con.close()

def convertLead(Id):
    con = sqlite3.connect('sales.db')
    cur = con.cursor()
    cur.execute(f'UPDATE Leads SET IS_CONVERTED=True WHERE LEAD_ID={Id}')
    con.commit()
    con.close()

def addCustomerData(ID, NAME, EMAIL, PHONE_NO):
    con = sqlite3.connect("sales.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Customers VALUES(NULL, ?,?,?)", (NAME, EMAIL, PHONE_NO))
    con.commit()
    con.close()
    
def addOrderData(CUST_ID, SUBTOTAL, DISCOUNT):
    con = sqlite3.connect("sales.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Orders VALUES(NULL, ?,?,?,?)", (CUST_ID, SUBTOTAL, DISCOUNT, (SUBTOTAL - (DISCOUNT / 100) * SUBTOTAL)))
    con.commit()
    con.close()

#======================================================FETCHING-DATA=========================================================================================================================

def fetchLeadData():
    con = sqlite3.connect("sales.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM Leads')
    rows = cur.fetchall()
    con.close()
    return rows

def fetchCustomerData():
    con = sqlite3.connect("sales.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM Customers')
    rows = cur.fetchall()
    con.close()
    return rows

def fetchOrderData():
    con = sqlite3.connect("sales.db")
    cur = con.cursor()
    cur.execute('SELECT * FROM Orders')
    rows = cur.fetchall()
    con.close()
    return rows
