from sqlalchemy import String, Column, Integer, ForeignKey, create_engine, select
from sqlalchemy.orm import registry, relationship, Session

engine = create_engine('mysql+mysqlconnector://root:sqltoshell@localhost:3306/shelf', echo = False)

mapper_registry = registry()

Base = mapper_registry.generate_base()

class Author(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key = True)
    first_name = Column(String(length = 25))
    last_name = Column(String(length = 25))

    def __repr__(self):
        return f'<Authors(author_id = {self.author_id}, first_name = {self.first_name}, last_name = {self.last_name})>'

class Book(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key = True)
    title = Column(String(length = 40))
    number_of_pages = Column(Integer)

    def __repr__(self):
        return f'<Books(book_id = {self.book_id}, title = {self.title}, number_of_pages = {self.number_of_pages})>'

class BA(Base):
    __tablename__ = 'authorsNbooks'
    id = Column(Integer, primary_key = True)
    book_id = Column(Integer, ForeignKey('books.book_id')) #mention the real table name here.
    author_id = Column(Integer, ForeignKey('authors.author_id'))

    author = relationship('Author') #as relationship() method is from orm, use the table model name here.
    book = relationship('Book')

    def __repr__(self):
        return f'<Authors_N_Books(id = {self.id}, author_id = {self.author_id}, book_id = {self.book_id})>'

Base.metadata.create_all(engine)

def add_book(book_json: Book, author_json: Author): #book_json the obj of BookSchemas is now also a type of Book class model, 
    with Session(engine) as session:
        existing_book = session.execute(select(Book).filter(Book.title==book_json.title, Book.number_of_pages==book_json.number_of_pages)).scalar()
        if existing_book is not None:
            print('Book already exists.')
            return

        print('Book does not exist, adding book...')
        session.add(book_json)

        existing_author = session.execute(select(Author).filter(Author.first_name==author_json.first_name, Author.last_name==author_json.last_name)).scalar()
        if existing_author is not None:
            print("Author already exist.")            
            session.flush()
            pairing = BA(book_id = book_json.book_id, author_id = existing_author.author_id)
        else:
            print('Author does not exist, adding book with author...')
            session.add(author_json)
            session.flush()
            pairing = BA(book_id = book_json.book_id, author_id = author_json.author_id)

        print("Adding pairing...")
        session.add(pairing)
        session.commit()
        print('New pairing ' + str(pairing))

def retrieve_book(id : int, first_name: str):
    with Session(engine) as session:
        if id is None: # This does not work.
            author = session.execute(select(Author).filter(Author.first_name==first_name)).scalar()
            if author is None:
                raise Exception('Requested author name does not exist.')
            pairing = session.execute(select(BA).filter(BA.author_id==author.author_id)).scalar()
            book = session.execute(select(Book).filter(Book.book_id==pairing.book_id)).scalar()
            return (author, book)
        if first_name is None:
            book = session.execute(select(Book).filter(Book.book_id==id)).scalar()
            if book is None:
                raise Exception('Requested book does not exist.')
            pairing = session.execute(select(BA).filter(BA.book_id==id)).scalar()
            author = session.execute(select(Author).filter(Author.author_id==pairing.author_id)).scalar()
            return (book, author)