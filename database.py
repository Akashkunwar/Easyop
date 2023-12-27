import sqlalchemy
from sqlalchemy import create_engine, text
import os

db_conn_str = os.environ['DB_CONN_STR']

engine = create_engine(
    db_conn_str,
    connect_args={
        "ssl" : {
        "ca": "cacert-2023-12-12.pem"}})

def load_inventories_from_DB():
    with engine.connect() as conn:
        result = conn.execute(text("select * from inventory"))
        result_all = result.all()
        inventor_dict = []
        for x in range(len(result_all)):
            columns = result.keys()
            row_dict = dict(zip(columns, result_all[x]))
            inventor_dict.append(row_dict)

def load_inventory_from_DB(id):
    with engine.connect() as conn:
        result = conn.execute(text(f"select * from inventory where Id={id}"))
        result_all = result.all()
        if len(result_all)==0:
            return None
        else:
            for x in range(len(result_all)):
                columns = result.keys()
                row_dict = dict(zip(columns, result_all[x]))
                return row_dict