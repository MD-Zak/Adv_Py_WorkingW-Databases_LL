#Inserting values into the database.
import psycopg2 as psy

if __name__ == '__main__':
    conn = psy.connect(database= 'red30',
                    user = 'postgres',
                    password = 'sqltopostgre',
                    host = 'localhost',
                    port = 5432)

    cursor = conn.cursor()

    # cursor.execute('''CREATE TABLE SALES
    #                     (ORDER_NUM INT PRIMARY KEY, 
    #                     CUST_NAME TEXT, 
    #                     PROD_NUMBER TEXT,
    #                     PROD_NAME TEXT,
    #                     QUANTITY INT, 
    #                     PRICE REAL, 
    #                     DISCOUNT REAL, 
    #                     ORDER_TOTAL REAL);''')

    sales = [(123098, "Oliver quinn", 786101, 'New quadcopter D4X4', 38, 8999.99, 0.145, 292409.6751),
    (123087, "Jason hanson", 786202, 'rustic rustbucket', 145, 15.99, 0.3, 2248.9935),
    (123076, "Daniel jack", 758402, 'brand new magicpump', 50, 224.509, 0.21, 8867.75),
    (123321, "Bangd convit", 121242, 'unwearable wristwatch', 199, 1349.99, 0.1, 265961.5299)]

    cursor.executemany('INSERT INTO SALES VALUES(%s, %s, %s, %s, %s, %s, %s, %s)', sales)

    conn.commit()
    conn.close()