"""
    날짜 : 2020-06-24
    이름 : 김나연
    내용 : 파이썬 데이터베이스 프로그래밍
"""

import pymysql as db

conn = db.connect(host='192.168.44.46',
                  user='kny',
                  password='1234',
                  db='kny',
                  charset='utf8')

cur = conn.cursor()
cur.execute("SELECT * FROM `USER1`")

for row in cur.fetchall():
    print('-------------------')
    print('아이디 : ', row[0])
    print('이름 : ', row[1])
    print('휴대폰 : ', row[2])
    print('나이 : ', row[3])
    print('-------------------')

conn.close()



