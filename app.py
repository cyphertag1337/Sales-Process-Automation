# imports
from flask.helpers import url_for
import db
import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return flask.render_template('homepage.html')

@app.route('/leads', methods=['GET'])
def leads_page():
    leads = db.fetchLeadData()
    return flask.render_template('leads_page.html', leads = leads)

@app.route('/customers', methods=['GET'])
def customers_page():
    customers = db.fetchCustomerData()
    return flask.render_template('customers_page.html', customers = customers)

@app.route('/leads/convert/<id>', methods=['GET'])
def convert_lead(id):
    print('Converted -->' + str(id))
    db.convertLead(id)
    return flask.redirect(url_for('leads_page'))

# @app.route('/order/new/<cust_id>', methods=['GET'])
# def add_order(cust_id):
#     print('Ordered For -->' + str(cust_id))
#     db.

@app.route('/leads/new', methods=['GET', 'POST'])
def new_lead():
    return flask.render_template('new_lead.html')

if __name__ == '__main__':

    # # set up tables
    # db.createLeadTable()
    # db.createCustomerTable()
    # db.createOrderTable()

    # # test data
    # db.addLeadData('Carol Shelby', 'cshel@shelby.com', '8860119033', 'Warm Hot', False)
    # db.addLeadData('Ken Miles', 'kmiles@shelby.com', '9711051129', 'Warm Hot', False)
    # db.addOrderData(1, 100, 20)

    # # debug
    # print(db.fetchLeadData())
    # print(db.fetchCustomerData())
    # print(db.fetchOrderData())

    app.run(debug=True)