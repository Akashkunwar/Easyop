from flask import  Flask, render_template, jsonify, request
from database import engine, load_inventory_from_DB, load_inventories_from_DB, add_inventory_to_db
from sqlalchemy import text

app = Flask(__name__)

def load_inventories_from_DB():
    with engine.connect() as conn:
        result = conn.execute(text("select * from inventory"))
        result_all = result.all()
        inventory_dict = []
        for x in range(len(result_all)):
            columns = result.keys()
            row_dict = dict(zip(columns, result_all[x]))
            inventory_dict.append(row_dict)
        return inventory_dict

@app.route('/')
def hello_easyop():
    inventory=load_inventories_from_DB()
    return render_template('home.html', inventory=inventory, companyName = 'EasyOP')

@app.route('/api/inventory')
def list_inventory():
    inventory=load_inventories_from_DB()
    return jsonify(inventory)

# @app.route("/api/inventory/<Id>")
# def show_inventory(Id):
#     inventory = load_inventory_from_DB(Id)
#     return jsonify(inventory)

@app.route("/inventory/<Id>")
def show_inventory(Id):
    inventory = load_inventory_from_DB(Id)
    if not inventory:
        return "Not Found", 404
    return render_template('inventory.html', inventory=inventory)

@app.route("/AddInventory")
def add_inventory():
    return render_template('AddInventory.html')

@app.route("/AddInventory/Submitions", methods=['post'])
def add_to_inventory():
    data = request.form
    return jsonify(data)
    add_inventory_to_db(data)
    return render_template('InventoryAdded.html', data=data)

if __name__ == "__main__":
    app.run()