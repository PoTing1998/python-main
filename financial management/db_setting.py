import sqlite3

conn = sqlite3.connect('datafile.db')
cursor = conn.cursor()

cursor.execute(
    """create table cash(transaction_id integer primary key, Taiwan_dollar integer, US_dollar real , note varchar(30), date_info date)""")

cursor.execute(
    """create table stock(transaction_id integer primary key, stock_id varchar(10), stock_num integer , stock_price real ,processing_fee real, tax integer, date_info date)""")



conn.commit() 
conn.close()