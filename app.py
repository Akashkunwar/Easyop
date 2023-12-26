from flask import  Flask, render_template

app = Flask(__name__)

inventory = [{'id':1,
         'Item':'Vivo v2',
         'Color':'Red',
         'Price':'Rs. 34000'},
         {'id':2,
         'Item':'Moto G2',
         'Price':'Rs. 44000'},
         {'id':3,
         'Item':'Iphone 14 pro max',
         'Color':'Black',
         'Price':'Rs. 134000'},
         {'id':4,
         'Item':'Realme GT Master',
         'Color':'Purple',
         'Price':'Rs. 30000'}]
 
@app.route('/')
def hello_world():
    return render_template('home.html', inventory=inventory, companyName = 'EasyOP')

if __name__ == "__main__":
    app.run()