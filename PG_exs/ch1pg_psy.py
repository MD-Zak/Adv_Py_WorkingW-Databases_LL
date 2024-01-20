#PG challenge: create a db, and 3 tables. Insert 3 books. Perform CRUD.

# Using just DBAPI
# import psycopg2 as psy
# if __name__ == '__main__':
#     conn = psy.connect(database = 'shelf',
#         host = 'localhost', port = 5432, user = 'postgres', password = 'sqltopostgre')
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE Books(
#             id INT PRIMARY KEY,
#             title TEXT,
#             nop INT);''')    
#     cursor.execute('''CREATE TABLE AuthorBooks(
#         id INT PRIMARY KEY,
#         author_id INT,
#         book_id INT);''')
#     cursor.execute('''CREATE TABLE Author(
#         id INT PRIMARY KEY,
#         first_name TEXT,
#         last_name TEXT);''')
    
#     books = [(305-1, 'Life of the river Nile', 4244), (305-2, 'Resurrection on the continential mail', 505)]
#     cursor.executemany('INSERT INTO Books VALUES(%s, %s, %s);', books)
#     cursor.execute('SELECT * FROM Books;')
#     print(cursor.fetchall())
#     conn.commit()
#     conn.close()

# # # Using sqlalchemy CORE(Expression language)
    # import sqlalchemy

    # engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:sqltopostgre@localhost/shelf')

    # metadata = sqlalchemy.MetaData()

    # authors_tab_obj = sqlalchemy.Table('author', metadata, 
    # sqlalchemy.Column('id', sqlalchemy.Integer),
    # sqlalchemy.Column('first_name', sqlalchemy.Text),
    # sqlalchemy.Column('last_name', sqlalchemy.Text))

    # metadata.create_all(engine) # metadata obj is used to instantiate the table obj.

    # with engine.connect() as conn:
    #     add = ((44011, 'cagatha', 'agrsthi'),(44022, 'ban', 'drown'))
    #     conn.execute(authors_tab_obj.insert().values(add)) # Add addressing used, such that multiple records can be inserted with a single query.
    #     conn.commit() #records or saves the changes directly to the db.
    #     # conn.execute(authors_tab_obj.delete().where(authors_tab_obj.c.ID == 44011))
    #     # conn.execute(authors_tab_obj.delete().where(authors_tab_obj.c.ID == 44022))
    #     # conn.commit()
    #     print(list(conn.execute(authors_tab_obj.select())))

# ## Using Sqlalchemy ORM w/ automap
#     from sqlalchemy import create_engine, select, text
#     from sqlalchemy.orm import Session
#     from sqlalchemy.ext.automap import automap_base

#     engine = create_engine('postgresql+psycopg2://postgres:sqltopostgre@localhost/shelf')

#     Base = automap_base()
#     Base.prepare(autoload_with = engine)
#     author_books = Base.classes.authorbooks # Autoloaded authorbooks table to create author_books model.

#     with Session(engine) as session:
#         # a_b = [author_books(id = 501, author_id = 44011, book_id = 304),
#         #  author_books(id = 502, author_id = 44022,book_id = 303)]
#         # session.bulk_save_objects(a_b)
#         # session.commit()
#         # session.flush()
#         print(list(session.execute(text('SELECT * FROM authorbooks;'))))

# ----------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------

from sqlalchemy import select, create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, registry, Session

engine = create_engine('postgresql://postgres:sqltopostgre@localhost/shelves')

mapper_registry = registry()
Base = mapper_registry.generate_base()

def insert_bok(tle, nop, f, l):

    author = Authors(first_name = f, last_name = l)
    book = Books(title = tle, number_of_pages = nop)

    with Session(engine) as session:

        existing_book = session.execute(select(Books).filter(Books.title == tle)).scalar()
        if existing_book is not None:            
            print('Book already exists.')
            return
        
        print('Book does not exist. Adding book...\n')
        session.add(book)

        existing_author = session.execute(select(Authors).filter(Authors.first_name == f, Authors.last_name == l)).scalar()
        if existing_author is not None:
            print('Author already exists. Not adding author\n')
            session.flush()
            pairing = Pub(book_id = book.id, author_id = existing_author.id)
            print('Adding pairing...\n')
        else:
            print('Author does not exist. Adding Author...\n')
            session.add(author)
            session.flush()
            pairing = Pub(author_id = author.id, book_id = book.id)
            print('Adding pairing...\n')

        # if session.execute(select(Pub).filter(book_id == Books.id, author_id = Authors.id)).scalar() is not None:
        #     print("pub entry already exists.\n")
        # elif session.execute(select(Pub).filter(book_id == Books.id)).scalar() is not None:
        #     session.add(Pub(author_id = Authors.id, book_id = Books.id))
        # elif session.execute(select(Pub).filter(author_id == Authors.id)).scalar() is not None:
        #     session.add(Pub(author_id = Authors.id, book_id = Books.id))

        session.add(pairing)
        print(list(session.execute(select(Authors))))
        print(list(session.execute(select(Books))))
        print(list(session.execute(select(Pub))))
        session.commit()
        print('Book added successfully.')
        print('New paring' + str(pairing))
            

class Books(Base):
    __tablename__ = 'book' #The model name should be different to the original table. An additional S suffix suffices.
    #This is important so that the tables are accessible from the db in bg.

    id = Column(Integer, primary_key = True)
    title = Column(String(length = 50))
    number_of_pages = Column(String(length = 50))

    def __repr__(self):
        return f'<Books(id = {self.id}, title = {self.title}, number_of_pages = {self.number_of_pages})>'

class Authors(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key = True)
    first_name = Column(String(length = 25))
    last_name = Column(String(length = 25))

    def __repr__(self):
        return f'<Authors(id = {self.id}, first_name = {self.first_name}, last_name = {self.last_name})'

class Pub(Base):
    __tablename__ = 'pubs'
    id = Column(Integer, primary_key = True)
    author_id = Column(Integer, ForeignKey('author.id'))
    book_id = Column(Integer, ForeignKey('book.id'))

    _2authors = relationship('Authors')
    _2books = relationship('Books')

    def __repr__(self):
        return f'<Pub(id = {self.id}, author_id = {self.author_id}, book_id = {self.book_id})>'

Base.metadata.create_all(engine)

if __name__ == '__main__':

    with Session(engine) as session:
     
        print(list(session.execute(select(Authors))))
        print(list(session.execute(select(Books))))
        print(list(session.execute(select(Pub))))

    print("Input a book.\n")
    title = str(input('Enter book name.\n'))
    nop = int(input('\nEnter the number of pages in the book.\n'))
    first_name = str(input('\nEnter first name of the author.\n'))
    last_name = str(input('\nEnter last name of the author.\n'))

    print("\nInteracting...\n")
    insert_bok(title, nop, first_name, last_name)



    