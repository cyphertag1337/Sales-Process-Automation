#backend

import sqlite3

#====================================================TABLES===========================================================================================================================

def Lead_Data():
    con = sqlite3.connect("Salesforce.db")
    cur.execute("CREATE TABLE IF NOT EXISTS LEAD(LEAD_ID INTEGER PRIMARY KEY, NAME VARCHAR(50), EMAIL VARCHAR(20), PHONE_NO NUMBER(10), COMPANY TEXT, DESCRIPTION LONGTEXT)")
    con.commit()
    con.close()
    
def Account_Data():
    con = sqlite3.connect("Salesforce.db")
    cur.execute("CREATE TABLE IF NOT EXISTS ACCOUNTS(ACCOUNT_ID INTEGER, COMPANY TEXT)")
    con.commit()
    con.close()
    
def Contact_Data():
    con = sqlite3.connect("Salesforce.db")
    cur.execute("CREATE TABLE IF NOT EXISTS CONTACTS(CONTACT_ID INTEGER, CONTACT_NAME TEXT, EMAIL VARCHAR(20), PHONE_NO NUMBER(10), ACCOUNT_ID INTEGER)")
    con.commit()
    con.close()
    
def Order_Data():
    con = sqlite3.connect("Salesorce.db")
    cur.execute("CREATE TABLE IF NOT EXISTS ORDERS(ORDER_NO INTEGER, COMPANY TEXT, SUBTOTAL FLOAT(10), DISCOUNT FLOAT(10), GRAND_TOTAL FLOAT(10)")
    con.commit()
    con.close()
    
    
#======================================================FUNCTIONS=========================================================================================================================



def addLeadData(LEAD_ID, NAME, EMAIL, PHONE_NO, COMPANY, DESCRIPTION):
    con = sqlite3.connect("Salesforce.db")
    cur = con.cursor(*)
    cur.execute("INSERT INTO LEAD VALUES(NULL, ?,?,?,?,?)", LEAD_ID, NAME, EMAIL, PHONE_NO, COMPANY, DESCRIPTION)
    con.commit()
    con.close()
    
def addAccountData(ACCOUNT_ID, COMPANY):
    con = sqlite3.connect("Salesforce.db")
    cur = con.cursor(*)
    cur.execute("INSERT INTO ACCOUNTS VALUES(NULL, ?)",ACCOUNT_ID, COMPANY)
    con.commit()
    con.close()

def addContactData(CONTACT_ID, CONTACT_NAME, EMAIL, PHONE_NO, ACCOUNT_ID):
    con = sqlite3.connect("Salesforce.db")
    cur = con.cursor(*)
    cur.execute("INSERT INTO CONTACTS VALUES(NULL, ?,?,?)",CONTACT_ID, CONTACT_NAME, EMAIL, PHONE_NO, ACCOUNT_ID)
    con.commit()
    con.close()
    
def addOrderData(ORDER_NO, COMPANY, SUBTOTAL, DISCOUNT, GRAND_TOTAL):
    con = sqlite3.connect("Salesforce.db")
    cur = con.cursor(*)
    cur.execute("INSERT INTO ORDERS VALUES(NULL, ?,?,?,?,?)",ORDER_NO, COMPANY, SUBTOTAL, DISCOUNT, GRAND_TOTAL)
    con.commit()
    con.close()
    
def Quote_Page():
    con = sqlite3.connect("Salesforce.db")
    cur = con.cursor(*)
    cur.execute("SELECTE * FROM ORDERS")
    rows = cur.fetchall()
    con.close()
    return rows




