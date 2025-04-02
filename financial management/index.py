from flask import Flask, render_template, request,g,redirect
import sqlite3
import requests
import math

app = Flask(__name__)

import sqlite3
from flask import g

DATABASE = "datafile.db"  # 確保 Flask 連接的是這個檔案



@app.teardown_appcontext
def close_db(exception):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route('/')
def home():
    conn = get_db()
    cursor = conn.cursor()
    result = cursor.execute("select * from cash")
    cash_result = result.fetchall()
    #計算台幣美金的總和
    taiwanese_dollars=0
    us_dollars=0
    for data in cash_result:
        taiwanese_dollars += data[1]
        us_dollars += data[2]
    #取得匯率
    r = requests.get('https://tw.rter.info/capi.php')
    currency = r.json()

    #計算總和
    total = taiwanese_dollars + us_dollars * currency['USDTWD']['Exrate']

    data = {
        'total': total,
        'currency': currency['USDTWD']['Exrate'],
        'ud'   : us_dollars,
        'td'   : taiwanese_dollars
    }
    return render_template('index.html',data=data)

@app.route('/cash')
def cash_form():
    return render_template('cash.html')

@app.route('/cash',methods= ['POST'] )
def submit_cash():
    # 取得金額與日期資料
    taiwanese_dollars = 0
    us_dollars = 0
    if request.values['taiwanese-dollars'] != '':
        taiwanese_dollars = request.values['taiwanese-dollars']
    if request.values['us-dollars'] != '':
        us_dollars = request.values['us-dollars']
    note = request.values['note']
    date = request.values['date']

    #連接資料庫
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute("""insert into cash (taiwanese_dollars, us_dollars, note, date_info) values (?, ?, ?, ?)""",
                   (taiwanese_dollars, us_dollars, note, date))
    conn.commit()

    return redirect("/")

@app.route('/stock')
def stock_form():
    return render_template('stock.html')

if __name__ == '__main__':
    app.run(debug=True) 
