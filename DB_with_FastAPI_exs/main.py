from fastapi import FastAPI, HTTPException
from . import schemas
from . import database

app = FastAPI()

@app.get('/') #get() method is a REST standard to retrieve information from an endpoint.
#In this case, it gets the information from home route, denoted by "/"

def get_root():
    return "Welcome to books api!"

@app.post('/book/')
def create_book(request: schemas.bookauthorpayload):
     #request of type schemas.bookauthorpayload
# here request is a obj of bookauthorpayload class. Thus it is able to access book_json an obj of bookSchemas class and so forth.

    database.add_book(convert_bj_bm(request.book_json), convert_aj_am(request.author_json))
    return "New Book added " + request.book_json.title + " " + str(request.book_json.number_of_pages) + " New Author added " + request.author_json.first_name + " " + request.author_json.last_name

#converter code - this is used to convert the schemas in schemas.py to table schemas in database.py - this create loose coupling
# w/ front and back end.
def convert_bj_bm(bj_tb_convtd: schemas.BookSchema):  
    #bj_tb_convtd - the book schema obj to be converted into Book model class obj.
    return database.Book(title = bj_tb_convtd.title, number_of_pages = bj_tb_convtd.number_of_pages)
    #schemas obj book goes in, Book model class obj comes out.

def convert_aj_am(aj_tb_convtd: schemas.AuthorSchema):
    return database.Author(first_name = aj_tb_convtd.first_name, last_name = aj_tb_convtd.last_name)
    # schemas obj author goes in, Author model class obj comes out.

@app.get('/book/{id}/book/{fn}')
def get_book(id:int | None = None, fn:str | None = None):
    try:
        return database.retrieve_book(id, fn) 
    except Exception as e:
        print(e)
        raise HTTPException(status_code = 404, detail = repr(e))

