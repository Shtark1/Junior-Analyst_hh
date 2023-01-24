import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def get(self):
        with self.connection:
            result = self.cursor.execute("SELECT `issue_key`, `started_at`, `ended_at` FROM `history` WHERE `previous_status` = ?", ("Open",)).fetchall()
            return result