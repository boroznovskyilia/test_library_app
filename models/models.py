import uuid
from dataclasses import dataclass
from utils.enums import Status


@dataclass
class Book():
    title:str
    author:str
    year:int
    status:Status = Status.in_stock.value
    id: str = str(uuid.uuid4())


@dataclass
class Library():
    books: list[Book] = None

