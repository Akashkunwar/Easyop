from flask import  Flask, render_template, jsonify
from database import engine, load_inventory_from_DB, load_inventories_from_DB
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
    return render_template('inventory.html', inventory=inventory)

if __name__ == "__main__":
    app.run()