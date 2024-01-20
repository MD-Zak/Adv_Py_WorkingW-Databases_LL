#Connecting python application with sqlalchemy core for postgresDb. and performing CRUD operations.
from sqlalchemy import create_engine, MetaData, Table, select

engine = create_engine('postgresql+psycopg2://postgres:sqltopostgre@localhost/red30')
metadata = MetaData() #metadata obj is used to keep track of the different tables we use.


sales_table = Table('sales', metadata, autoload_with = engine) #To create a table obj; autoload_with is used. As a table already exists.
#We pass in the metadata obj, as it acts as a dictionary that stores a series of tables, 
#where the tablename is the key and the value is the table obj.

metadata.create_all(engine) #Instantiating the table using the metadata obj.

with engine.connect() as conn:

    #read
    for row in conn.execute(select(sales_table)):
        print(row)

    #create
    insert_stmt = sales_table.insert().values(order_num = 110101,
    cust_name = 'James bottomups',
    prod_number = 'B110',
    prod_name = 'Decoding water',
    quantity = 8,
    price = 3.1415,
    discount = 0.02718,
    order_total = 24.448)
    conn.execute(insert_stmt)

    new_ord_slct = sales_table.select().where(sales_table.c.order_num == 110101)
    print('\n')
    print("YO")
    print(list(conn.execute(new_ord_slct)),'\n') #first() is used to retrieve the first result/record in a iterator set.
    # Result can also be printed using the list(). Converting the result to a list type, similar to psycopg2 cursor result.
    #where cur.fetchall() does the latter by default.
    # for row in conn.execute(new_ord_slct):
    #     print(row, '\n')

    #update
    updt_stmt = sales_table.update().where(sales_table.c.order_num == 110101).values(quantity = 88, order_total = 268.938)
    conn.execute(updt_stmt)

    #Confirm update
    print(conn.execute(new_ord_slct).first(),'\n')

    #Delete
    del_stmt = sales_table.delete().where(sales_table.c.order_num == 110101)
    conn.execute(del_stmt)

    #Confirm delete
    print(conn.execute(new_ord_slct).rowcount) #Will print the rowcount as 0 is no result.
    # print(tuple(conn.execute(select(sales_table)))) #Works as it is a sales_obj. Correction, works because as the result would be a cursorresult set,
    # as a connection obj is used.