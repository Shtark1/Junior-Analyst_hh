import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def get(self):
        with self.connection:
            result = self.cursor.execute("SELECT `issue_key`, `previous_status`, `started_at` FROM `history` WHERE `previous_status` != ? and `previous_status` != ?", ("Closed", "Resolved")).fetchall()
            return result