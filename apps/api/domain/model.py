from datetime import datetime
from typing import Union


class Book:
    def __init__(
        self,
        title: str,
        author: str,
        publisher: str,
        pages: int,
        created_at: Union[datetime, None] = None,
        updated_at: Union[datetime, None] = None,
    ):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.created_at = created_at if created_at else None
        self.updated_at = updated_at if updated_at else None

    def to_dict(self):
        return dict(
            title=self.title,
            author=self.author,
            publisher=self.publisher,
            pages=self.pages,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )


class Tag:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name