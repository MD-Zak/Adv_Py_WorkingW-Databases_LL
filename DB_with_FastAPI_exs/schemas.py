from pydantic import BaseModel

class BookSchema(BaseModel):
    title: str
    number_of_pages: int

class AuthorSchema(BaseModel):
    first_name: str 
    last_name: str

class bookauthorpayload(BaseModel):
    book_json : BookSchema
    author_json: AuthorSchema

class idschema(BaseModel):
    id : int