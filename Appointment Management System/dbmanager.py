import sqlite3

class DatabaseManager:
    global conn
    global tmp
    def connectDatabase(self):
        try:
            self.tmp = sqlite3.connect("lifeline.db")
            self.conn=self.tmp.cursor()
        except Exception as e:
            raise e


    def execute(self,query:str):
        try:
            #print(query)
            self.conn.execute(query)
            return self.conn.fetchall()
        except Exception as e:
            raise  e

    def coomitChanges(self):
        try:
            self.tmp.commit()
        except Exception as e:
            raise e

    def connection_close(self):
        self.conn.close()
