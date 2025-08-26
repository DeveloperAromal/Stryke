import psycopg2


class Database:
    def __init__(self, dsn):
        self.dsn = dsn
        self.conn = None
        
    def connect(self):
        if not self.conn:
            self.conn = psycopg2.connect(self.dsn)
            
        return self.conn
            
            
    def excecute(self, query, params = None):
        
        with self.connect().cursor as cursor:
            cursor.execute(query, params)
            
            try:
                return cursor.fetchall()
            
            except:
                return None
            
                        
    def commit(self):
        self.conn.commit()