import sqlite3 as sql

admindb = sql.connect("admin.db")
admindb = sql.connect("products.db")
admindb = sql.connect("cart.db")
with sql.connect("admin.db") as con:
    pen = con.cursor()
    pen.execute("""CREATE TABLE IF NOT EXISTS carts(
                user_id TEXT,
                email TEXT,
                nickname TEXT,
                password TEXT,
                phone INTEGER
    )""")
    pen.execute("SELECT  * FROM carts") 

with sql.connect("products.db") as con:
    pen = con.cursor()
    pen.execute("""CREATE TABLE IF NOT EXISTS carts(
                image BLOB,
                name TEXT,
                description TEXT
    )""")
    pen.execute("SELECT  rowid, * FROM carts") 

with sql.connect("cart.db") as con:
    pen = con.cursor()
    pen.execute("""CREATE TABLE IF NOT EXISTS carts(
                count INTEGER
    )""")
    pen.execute("SELECT  * FROM carts") 