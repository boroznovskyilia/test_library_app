import enum

class SearchFields(enum.Enum):
    TITLE = "title"
    AUTHOR = "author"
    YEAR = "year"


class Status(enum.Enum):
    in_stock = "в наличии"
    given = "выдана"