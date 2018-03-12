import sqlite3
from pathlib import Path

dbName = 'math.db'

def initData():
    # create tabel and do the data initializision for table math_plus
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    c.execute('''CREATE TABLE math_plus(left int, right int, sum int)''')
    purchases = []
    left = 0
    right = 0
    insertSQL = "INSERT INTO math_plus VALUES (?,?,?)"
    for x in range(100):
        for y in range(100):
            left = x + 1
            right = y + 1
            purchases.append((left, right, left+right))
        c.executemany(insertSQL, purchases)
        conn.commit()
        purchases.clear()
    conn.close()

def isDBExists():
    p = Path(dbName)
    return p.exists()

def getBelow(num):
    # get plus statements for both left and right below num
    if not isDBExists():
        initData()
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    sql = "SELECT * FROM math_plus WHERE left < ? and right < ?"
    statements = []
    resultSet = c.execute(sql, (num, num))
    for row in resultSet:
        statements.append([x for x in row])
    conn.close()
    return statements

def getSumBelow(num):
    if not isDBExists():
        initData()
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    sql = "SELECT * FROM math_plus WHERE sum <= ?"
    statements = []
    resultSet = c.execute(sql, (num,))
    for row in resultSet:
        statements.append([x for x in row])
    conn.close()
    return statements