'''
Created on 2021. 7. 22.

SQLite의 CRUD (C - Create(or Insert), R - Select, U - Update, D - Delete)
각 기능을 함수로 만들 수 있다.

@author: pc356
'''

import sqlite3

def createTable():
    # connection 객체 생성
    conn = sqlite3.connect('test.db') # isolation_level = None 생략
    
    # cursor 생성
    c = conn.cursor()
    c.execute('''
        create table if not exists mymember
        (id text primary key,
        name text,
        password text,
        remark text)
    ''')
    # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    pass

# insert할 매개 변수    
def insertData(id, name, password, remark):
    conn = sqlite3.connect('test.db')
    
    c = conn.cursor()
    c.execute('''
        insert into mymember(id, name, password, remark)
        values(?, ?, ?, ?)
    ''',(id, name, password, remark))# 매개 변수를 질의문에 넣는 방법
    
    # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    pass

def insertManyData(tupleData):
    conn = sqlite3.connect('test.db')
    
    c = conn.cursor()
    c.executemany('''
        insert into mymember(id, name, password, remark)
        values(?, ?, ?, ?)
    ''',tupleData)# 매개 변수를 질의문에 넣는 방법
    
    # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    pass

def selectAll():
    conn = sqlite3.connect('test.db')

    c = conn.cursor()
    c.execute('select * from mymember')
    
    rows = c.fetchall()
    
    # # 1방식
    # print('-1방식으로 출력')
    # print(c.fetchall()) # 결과가 여러줄 일 경우 fetchall() 사용 
    # readData = c.fetchall()
    # for row in readData:
    #     print(row)
    
    # # 2방식    
    # print('-2방식으로 출력')
    # for row in c.execute('select * from mymember'):
    #     print(row)
        
    # # 3방식
    # print('-3방식으로 출력')
    # c.execute('select * from mymember')
    # print(c.fetchall())
    
    # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    return rows

    pass

def select(key):
    conn = sqlite3.connect('test.db')
    
    c = conn.cursor()
    c.execute('select * from mymember where id = ?',(key,)) # key - tuple 형식, 유의
    
    # print(c.fetchone()) # 결과가 한줄 일 경우 fetchone() 사용
    
    row = c.fetchone()
    
    # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    return row
    
    pass

# vo는 dict로 만들어서 보냄
def update(vo): # vo는 tuple 형식임
    conn = sqlite3.connect('test.db')
    
    c = conn.cursor()
    c.execute('''
        update mymember set name = ?, password = ?, remark = ? where id = ?
    ''',vo) # vo - tuple 형식(dict일 경우 복잡함.), 유의
    
     # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    pass

def delete(key):
    conn = sqlite3.connect('test.db')
    
    c = conn.cursor()
    res = c.execute('''delete from mymember where id = ?''',(key,)) # key - tuple 형식, 유의
    
    # if len(list(res)) == 0: # 자료가 없다면,
    #     return -1
    
     # isolation_level = None 생략 - cursor, connection 객체 close()
    conn.commit()
    
    c.close()
    
    conn.close()
    
    # return len(list(res))
    
    pass    
    
    
    
    
    
    