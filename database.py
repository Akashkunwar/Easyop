import sqlalchemy
from sqlalchemy import create_engine, text
import os

# with open('D:\Project\Easyop\env.txt', 'r') as f:
#     db_conn_str = f.read()
# print(db_conn_str)

db_conn_str = os.environ['DB_CONN_STR']

# db_conn_str = "mysql+pymysql://2kmr91fsicqq9bbrq2am:pscale_pw_ijHbJNgRvL8MMwjNPB69ihUzrMx2SkeMkW6XNxedw77@aws.connect.psdb.cloud/easyop?charset=utf8mb4"

engine = create_engine(
    db_conn_str,
    connect_args={
        "ssl" : {
        "ca": "Easyop\cacert-2023-12-12.pem"}})

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

# conn = engine.connect()
# result = conn.execute(text("select * from inventory"))
# result_all = result.all()

# # print("typeResult : ", type(result))
# # print(result)

# # print("typeResultAll : ", type(resultall))
# # print(resultall)
# # print(dict(resultall[0]))
# # frd = dict(result_all[0])

# # if result_all:
# #     columns = result.keys()  # Get column names
# #     first_row_dict = dict(zip(columns, result_all[0]))  # Convert first row to a dictionary

# result_dict = []
# for x in range(len(result_all)):
#     columns = result.keys()  # Get column names
#     row_dict = dict(zip(columns, result_all[x]))  # Convert first row to a dictionary
#     result_dict.append(row_dict)

# print(result_dict)
# print(type(result_dict))
# conn.close()
