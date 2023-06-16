from sqlite3 import connect

class DataBase(object):
    def __init__(self, dbname):
        self.conn = connect(dbname + '.db')
        self.cursor = self.conn.cursor()

    def createTable(self, tbname, attributes = {}):
        command = 'CREATE TABLE IF NOT EXISTS ' + tbname + '('

        for key, value in attributes.items():
            command = command + key + ' ' + value + ','
            
        command = command + ');'
        
        self.cursor.execute(command)
        self.conn.commit()
        
    def insertInTable(self, table, values):
        command = 'INSERT INTO ' + table + 'VALUES ('
        
        for value in values:
            command = command + str(value) + ','
        
        command = command + ');'
        
        self.cursor.execute(command)
        self.conn.commit() 

db1 = DataBase('test')