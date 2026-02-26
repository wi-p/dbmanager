from sqlite3 import connect

class DataBase(object):
    def __init__(self, dbname):
        self.conn = connect(dbname + '.db')
        self.cursor = self.conn.cursor()

    def createTable(self, tbname, attributes = ()):
        command = 'CREATE TABLE IF NOT EXISTS ' + tbname + '(' + str(attributes)[1:] + ';'

        self.cursor.execute(command)
        self.conn.commit()
        
    def insertInTable(self, table, values):
        command = 'INSERT INTO ' + table + ' VALUES (' + ((len(values) -1) * '?,') +  '?);'

        self.cursor.execute(command, values)
        self.conn.commit() 

    def readTable(self, att, table):
        return self.cursor.execute('SELECT ' + att + ' FROM ' + table).fetchall()

db1 = DataBase('test')
db1.createTable('Student', ('name VARCHAR', 'age INTEGER'))
db1.insertInTable('Student',('ana', 15))

print(db1.readTable('*','Student'))