from flask import Flask, render_template, request,g,redirect
import sqlite3
import requests
import math
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')  # 使用非互動式後端


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
    #取得匯率計算總和
    r = requests.get('https://tw.rter.info/capi.php')
    currency = r.json()
    total = math.floor(taiwanese_dollars + us_dollars * currency['USDTWD']['Exrate'])

    #取得股票資訊
    result2 = cursor.execute("select * from stock")
    stock_result = result2.fetchall()
    unique_stock_list = []  
    for data in stock_result:
        if data[1] not in unique_stock_list:
            unique_stock_list.append(data[1])
    #計算股票總市值
    total_stock_value = 0
    #計算單一股票資訊
    stock_info = []
    for stock in unique_stock_list:
        result = cursor.execute("select * from stock where stock_id = ?", (stock,))
        result = result.fetchall()
        stock_cost = 0 #單一股票總花費
        shares = 0 #單一股票股數
    
        for d in result:
            shares += d[2]
            stock_cost += d[3] * d[2] + d[4] + d[5]
        #取地目前股價
        url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&stockNo=" + stock

        response = requests.get(url)
        data = response.json()
        price_array = data['data']
        current_price =float( price_array[len(price_array)-1][6])

        #單一股票總市值
        total_value =round( shares * current_price)
        total_stock_value += total_value
        #單一股票平均成本
        average_cost = round(stock_cost / shares,2)
        #單一股票報酬率
        rate_of_return = round((total_value - stock_cost)*100 / stock_cost,2 )
    
    for stock in stock_info:
        stock['value_percentage'] = round(stock['total_value'] * 100 / total_stock_value, 2)

    if len(unique_stock_list)!= 0:
        labels= tuple(unique_stock_list)
        sizes= [d[total_value] for d in stock_info]
        





    data = {
        'total': total,
        'currency': currency['USDTWD']['Exrate'],
        'ud'   : us_dollars,
        'td'   : taiwanese_dollars,
        'cash_result': cash_result,
        stock_info: stock_info,
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

@app.route('/cash-delete', methods=['POST'])
def cash_delete():
    transaction_id = request.value['id']
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""delete from cash WHERE transaction_id = ?""", (transaction_id,))

    conn.commit()
    return redirect("/")


@app.route('/stock')
def stock_form():
    return render_template('stock.html')

@app.route('/stock', methods=['POST'])
def submit_stock():
    # 取得股票資訊與日期資料
    stock_id = request.values['stock-id']
    stock_num = request.values['stock-num']
    stock_price = request.values['stock-price']
    processing_fee =0
    tax=0
    if request.values['processing-fee'] != '':
        processing_fee = request.values['processing-fee']
    if request.values['tax'] != '':
        tax = request.values['tax']
    date = request.values['date']

    #連接資料庫
    #連接資料庫
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute("""insert into cash (stock_id, stock_num, stock_price,processing_fee,tax, date_info) values (?, ?, ?, ?,?, ?)""",
                (stock_id, stock_num, stock_price, processing_fee, tax, date))
    conn.commit()

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True) 
