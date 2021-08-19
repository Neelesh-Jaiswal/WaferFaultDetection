import sqlite3
# from DataTypeValidation_Insertion_Training.DataTypeValidation import dBOperation


# conn = dBOperation.dataBaseConnection('sqlite_master')
conn = sqlite3.connect('Training.db')
c = conn.cursor()

def read_from_db():
    c.execute("Select * from sqlite_master")
    data = c.fetchall()
    print(data)
    # for i in c.fetchall():
    #     print(i)

if __name__ == '__main__':
    read_from_db()
    c.close()
    conn.close()


