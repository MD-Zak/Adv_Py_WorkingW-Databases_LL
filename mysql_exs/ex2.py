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

def add_proj_and_tasks(cursor, project_title, project_description, tasks):
    project_data = (project_title, project_description)
    cursor.execute('''INSERT INTO Projects(title, description)
        VALUES(%s, %s)''', project_data)
    tasks_data = []
    for task in tasks:
        task_data = (cursor.lastrowid, task)
        tasks_data.append(task_data)
    cursor.executemany('''INSERT INTO Tasks(project_id, description)
        VALUES(%s, %s)''', tasks_data)

if __name__ == '__main__':
    db = connect('projects')

    cursor = db.cursor()

    tasks = ['clean bathroom','clean kitchen','clean living room']
    #add_proj_and_tasks(cursor, 'clean house', 'clean house by room', tasks)
    #cursor.execute('DELETE FROM tasks WHERE project_id = 4;')
    #cursor.execute('DELETE FROM Projects WHERE project_id = 4;')
    db.commit()

    cursor.execute('SELECT * FROM Projects;')
    project_records = cursor.fetchall()
    print(project_records,'\n')

    cursor.execute('SELECT * FROM Tasks;')
    task_records = cursor.fetchall()
    print(task_records)
    
    db.close()