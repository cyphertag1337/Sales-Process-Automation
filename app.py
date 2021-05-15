# imports
import db
import flask
from flask.helpers import url_for

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

@app.route('/orders/<cust_id>', methods=['GET'])
def orders_page(cust_id):
    orders = db.fetchOrderData(cust_id = cust_id)
    return flask.render_template('orders_page.html', orders = orders, cust_id = cust_id)

@app.route('/leads/convert/<id>', methods=['GET'])
def convert_lead(id):
    db.convertLead(id)
    return flask.redirect(url_for('leads_page'))

@app.route('/orders/new/<cust_id>', methods=['GET', 'POST'])
def new_order(cust_id):
    if flask.request.method == 'POST':
        db.addOrderData(
            cust_id,
            float(flask.request.form['subtotal']),
            float(flask.request.form['discount'])
        )
        return flask.redirect(url_for('orders_page', cust_id=cust_id))
    else:
        return flask.render_template('new_order.html', cust_id=cust_id)

@app.route('/leads/new', methods=['GET', 'POST'])
def new_lead():
    if flask.request.method == 'POST':
        db.addLeadData(
            flask.request.form['name'],
            flask.request.form['email'],
            flask.request.form['phone'],
            flask.request.form['status'],
        )
        return flask.redirect(url_for('leads_page'))
    else:
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