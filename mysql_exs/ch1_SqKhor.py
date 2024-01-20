import mysql.connector as mysql

def connect(db_name): 
    try: 
        return mysql.connect(host = 'localhost', user = 'root', password = 'sqltoshell', database = db_name)
    except Error as e:
        print(e)

if __name__ == '__main__':

    db = connect('red30') #creates connection object.

    cursor = db.cursor() #Creates cursor object from the connection object.

    cursor.execute('SELECT * FROM Sales ORDER BY order_total DESC LIMIT 1;') #Returns the most expensive order.
    print(cursor.fetchall(),'\n')

    cursor.execute('SELECT cust_name FROM Sales ORDER BY order_total DESC LIMIT 1;')
    #Returns the customer name with most expensive order.
    print(cursor.fetchall())
    db.close()
