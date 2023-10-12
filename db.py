import sqlite3

DATABASE_Demend = 'Demend.db'
DATABASE_Supply = 'Supply.db'


def create_Receiver_list_table():
    con = sqlite3.connect(DATABASE_Demend)
    #db_Receiver_list = con.execute('DROP TABLE IF EXISTS Receiver_list')
    con.execute("CREATE TABLE IF NOT EXISTS Receiver_list(id,receiver_id,category,material,form,condition,weight,best_before,create_at,updated_at,memo)")
    con.close()


def create_Maker_list_table():
    con = sqlite3.connect(DATABASE_Supply)
    #db_Maker_list = con.execute('DROP TABLE IF EXISTS Maker_list')
    con.execute("CREATE TABLE IF NOT EXISTS Maker_list(id,maker_id,category,material,form,condition,weight,best_before,create_at,updated_at,memo)")
    con.close()