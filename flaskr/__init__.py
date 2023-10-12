from flask import Flask
app = Flask(__name__)
import flaskr.main

from flaskr import db
db.create_Receiver_list_table()
db.create_Maker_list_table()