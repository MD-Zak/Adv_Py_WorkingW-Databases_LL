#Connecting python app with SqAl ORM to PG db and perform CRUD with ORM.
from sqlalchemy import create_engine, select, text
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

engine = create_engine('postgresql+psycopg2://postgres:sqltopostgre@localhost/red30')

# mapper_registry = registry()
# Base = mapper_registry.generate_base()

# class Sales(Base):
    # __tablename__ = 'Sales'
    # Column('order_num', Integer),
    # Column('cust_name',String(length = 50)),
    # Column('prod_number',String(length = 30)),
    # Column('prod_name',String(length = 25)),
    # Column('quantity',Numeric),i
    # Column('price',Numeric),
    # Column('discount',Numeric),
    # Column('order_total',Numeric)

Base = automap_base()
Base.prepare(autoload_with = engine)

Sales = Base.classes.sales #autoloaded Sales table model, a repurcussion of ORM+, aka a concussion to my head.

with Session(engine) as session:

    #read
    smallest_sale = session.execute(select(Sales).order_by(Sales.order_total)).scalar()
    print(smallest_sale.order_total,'\n')

    #create/insert
    new_sale = Sales(order_num = 1100113, cust_name = 'Carolyn Cubefassad', prod_name = 'DownOnNotes notes')
    session.add(new_sale)
    session.commit()
    res = session.execute(select(Sales).where(Sales.order_num == 1100113)).scalar()
    print('\nFrom Insert')
    print(res.order_num)

    #update
    new_sale.quantity = 1021
    new_sale.order_total = 76.85
    print('\nFrom Update')
    print(res.quantity)
    session.commit()

    #delete
    # returned_sale = res
    session.delete(res)
    session.commit()
    print('\nFrom Delete')
    session.flush()
    # print(session.execute(text('SELECT * FROM Sales;')).first())

    # q = session.execute(select(Sales)).scalar()
    # This would not work as Sales is a automap obj. # Correction, did not work as it was a parameter to session obj.

    # print(q)

    print(engine.connect().execute(select(Sales)).first()) # Works now.
    engine.connect().close()

