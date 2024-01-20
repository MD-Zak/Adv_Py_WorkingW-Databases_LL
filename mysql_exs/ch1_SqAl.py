from sqlalchemy import Column, String, Integer, create_engine, select, text
from sqlalchemy.orm import registry, Session

engine = create_engine('mysql+mysqlconnector://root:sqltoshell@localhost:3306/red30',echo = False)

mapper_registry = registry() 

New_base = mapper_registry.generate_base()

class Sales(New_base):
    __tablename__ = 'Sales'
    order_num = Column(Integer, primary_key = True)
    order_type = Column(String(length = 25))
    cust_name = Column(String(length = 30))
    prod_category = Column(String(length = 100))
    prod_number =  Column(Integer)
    prod_name = Column(String(length = 100))
    quantity = Column(Integer)
    price = Column(Integer)
    discount = Column(Integer)
    order_total = Column(Integer)

    def __repr__(self):
        return "<Sales(Order_number = {0}, Customer_Name = {1}, product = {2}, Total_cost = {3})>".format(
            self.order_num, self.cust_name, self.prod_name, self.order_total)

New_base.metadata.create_all(engine)

with Session(engine) as session:
    # sttmt = text('SELECT cust_name FROM Sales ORDER BY order_total DESC LIMIT 1;')
    sttmt = select(Sales).order_by(Sales.order_total.desc())
    # results = session.execute(sttmt).scalar() #scalar() just returns the first record fetch from the db.
    # for r in results:
    print(session.execute(sttmt).scalar())
    session.commit()