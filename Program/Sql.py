import sqlite3
class Program:
    def __init__(self, con_string):
        try:
            self.con_string = con_string
            self.conn = sqlite3.connect(con_string)
            print("Connected To Database")
        except sqlite3.Error as e:
            print("[-] Error in Connection: ", e)
    def __del__(self):
            print("File Closed Successfuly!")
