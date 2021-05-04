# imports
import db
import flask

if __init__ == 'main':

    # set up tables
    db.createLeadTable()
    db.createCustomerTable()
    db.createOrderTable()

    # db.addLeadData('Shelby', 'cshel@shelby.com', '9999999999', 'Warm Hot', False)
    # db.convertLead(1)
    # db.addOrderData(1, 100, 20)

    # debug
    print(db.fetchLeadData())
    print(db.fetchCustomerData())
    print(db.fetchOrderData())