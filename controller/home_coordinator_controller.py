import pandas as pd

class CoordinatorControler:
    def __init__(self, root, connection):
        self.root = root
        self.conn = connection
        self.cursor = self.conn.cursor(dictionary=True)
    
    def get_scholarship_by_type(self):
        query = """
            SELECT scholarship_type, COUNT(*) as count
            FROM scholarship
            GROUP BY scholarship_type
            ORDER BY count DESC
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        
        df = pd.DataFrame(result)
        return df
        
    def get_scholarship_by_course(self):
        query = """
            SELECT course, COUNT(*) as count
            FROM scholarship
            GROUP BY course
            ORDER BY count DESC
            LIMIT 15
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        
        df = pd.DataFrame(result)
        return df
        
    def get_scholarship_by_gender(self):
        query = """
            SELECT gender, COUNT(*) as count
            FROM scholarship
            GROUP BY gender
            ORDER BY count DESC
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        
        df = pd.DataFrame(result)
        return df
        
    def get_scholarship_by_race(self):
        query = """
            SELECT race, COUNT(*) as count
            FROM scholarship
            GROUP BY race
            ORDER BY count DESC
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        
        df = pd.DataFrame(result)
        return df