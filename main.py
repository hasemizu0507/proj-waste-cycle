from flaskr import app
from flask import render_template,request,redirect,url_for
import sqlite3
import random, string

DATABASE_Demend = 'Demend.db'
DATABASE_Supply = 'Supply.db'
user_Rid = 1
user_Mid = 1


@app.route('/')
def Select():
    return render_template(
        'Select.html',
    )

@app.route('/Maker')
def Maker():
    con = sqlite3.connect(DATABASE_Demend)
    db_Receiver_list = con.execute('select * from Receiver_list').fetchall()
    con.close()
    
    Receiver_list = []
    for row in db_Receiver_list:
        Receiver_list.append({'id':row[0],'receiver_id':row[1],'category':row[2],'material':row[3],'form':row[4],'condition':row[5],'weight':row[6],'best_before':row[7],'create_at':row[8],'updated_at':row[9],'memo':row[10]})
    
    return render_template(
        'Maker.html',
        Receiver_list = Receiver_list
    )

@app.route('/Receiver')
def Receiver():
    
    con = sqlite3.connect(DATABASE_Supply)
    db_Maker_list = con.execute('select * from Maker_list').fetchall()
    con.close()

    Maker_list = []
    for row in db_Maker_list:
        Maker_list.append({'id':row[0],'maker_id':row[1],'category':row[2],'material':row[3],'form':row[4],'condition':row[5],'weight':row[6],'best_before':row[7],'create_at':row[8],'updated_at':row[9],'memo':row[10]})
    
    return render_template(
        'Receiver.html',
        Maker_list = Maker_list
    )
  

@app.route('/Maker_edit')
def Maker_edit():

    con = sqlite3.connect(DATABASE_Supply)
    db_My_Mlist = con.execute('select * from Maker_list WHERE maker_id = "1"').fetchall()
    con.close()
    
    My_Mlist = []
    for row in db_My_Mlist:
        My_Mlist.append({'id':row[0],'maker_id':row[1],'category':row[2],'material':row[3],'form':row[4],'condition':row[5],'weight':row[6],'best_before':row[7],'create_at':row[8],'updated_at':row[9],'memo':row[10]})
    
    return render_template(
        'Maker_edit.html',
        My_Mlist = My_Mlist
    )

@app.route('/Receiver_edit')
def Receiver_edit():

    con = sqlite3.connect(DATABASE_Demend)
    db_My_Rlist = con.execute('select * from Receiver_list WHERE receiver_id = "1"').fetchall()
    con.close()
    
    My_Rlist = []
    for row in db_My_Rlist:
        My_Rlist.append({'id':row[0],'receiver_id':row[1],'category':row[2],'material':row[3],'form':row[4],'condition':row[5],'weight':row[6],'best_before':row[7],'create_at':row[8],'updated_at':row[9],'memo':row[10]})

    return render_template(
        'Receiver_edit.html',
        My_Rlist = My_Rlist
    )

@app.route('/register_MakerInfo',methods=['POST'])
def register_MakerInfo():
    category = request.form['category']
    material = request.form['material']
    form = request.form['form']
    condition = request.form['condition']
    weight = request.form['weight']
    best_before = request.form['best_before']
    create_at = request.form['create_at']
    updated_at = request.form['updated_at']
    memo = request.form['memo']

    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(8)]
    id = ''.join(randlst)
    receiver_id = user_Rid
    con = sqlite3.connect(DATABASE_Supply)
    con.execute('insert into Maker_list values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',[id, receiver_id,category,material,form,condition,weight,best_before,create_at,updated_at,memo])
    con.commit()
    con.close()
    return render_template(
        'Maker_edit.html',
    )

@app.route('/register_ReceiverInfo',methods=['POST'])
def register_ReceiverInfo():
    category = request.form['category']
    material = request.form['material']
    form = request.form['form']
    condition = request.form['condition']
    weight = request.form['weight']
    best_before = request.form['best_before']
    create_at = request.form['create_at']
    updated_at = request.form['updated_at']
    memo = request.form['memo']

    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(8)]
    id = ''.join(randlst)
    maker_id = user_Mid
    con = sqlite3.connect(DATABASE_Demend)
    con.execute('insert into Receiver_list values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',[id,maker_id,category,material,form,condition,weight,best_before,create_at,updated_at,memo])
    con.commit()
    con.close()
    return render_template(
        'Receiver_edit.html',
    )

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

