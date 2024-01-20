#Interacting with the db in a desired way.
import psycopg2

def insert_values(cur, order_num, cust_name, prod_number, prod_name, quantity, price, discount):
    order_total = quantity * price
    if discount != 0:
        order_total = discount * order_total
    sales_data = {
        "num" : order_num,
        "cust_name" : cust_name,
        "prod_number" : prod_number,
        "prod_name" : prod_name,
        "quantity" : quantity,
        "price" : price,
        "discount" : discount,
        "order_total" : order_total
    }
    cur.execute('''INSERT INTO sales VALUES( %(num)s, %(cust_name)s, 
        %(prod_number)s, %(prod_name)s, %(quantity)s, %(price)s, %(discount)s, %(order_total)s);''',sales_data)

if __name__ == '__main__':
    conn = psycopg2.connect(database = 'red30', host = 'localhost', port = 5432, user = 'postgres', password = 'sqltopostgre')
    cursor = conn.cursor()
    # print("Input sale data:\n")
    # order_num = int(input('Enter order number.\n'))
    # cust_name = input('Enter customer name.\n')
    # prod_number = input('Enter product number.\n')
    # prod_name = input('Enter product name.\n')
    # quantity = float(input('Enter order quantity.\n'))
    # price = float(input('Enter individual item price.\n'))
    # discount = float(input('Enter discount, if any else enter 0.\n'))
    # print('Inserting entered data...\n')
    # insert_values(cursor, order_num, cust_name, prod_number, prod_name, quantity, price, discount)
    cursor.execute('SELECT * FROM sales;')
    results = cursor.fetchall()
    print(results) # returns a result with type; list.
    conn.commit()
    conn.close()