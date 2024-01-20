#Adv Py: Working with databases, Lesson2, Author: Kat.

import mysql.connector as mysql

def connect(db_name):
    try:
        return mysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'sqltoshell',
            database = db_name)
    except Error as e:
        print(e)

if __name__ == '__main__':
    db = connect('projects')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Projects;")
    project_results = cursor.fetchall()
    print(project_results)
    db.close()
    
