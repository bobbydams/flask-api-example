from apps.api.domain import model


def test_book():
    book = model.Book(
        title="A Book", author="An Author", publisher="A Publisher", pages=1000
    )

    assert book.title == "A Book"
    assert book.author == "An Author"
    assert book.publisher == "A Publisher"
    assert book.pages == 1000


def test_book_to_dict():
    book_dict = model.Book(
        title="A Book", author="An Author", publisher="A Publisher", pages=1000
    ).to_dict()

    assert book_dict["title"] == "A Book"
    assert book_dict["author"] == "An Author"
    assert book_dict["publisher"] == "A Publisher"
    assert book_dict["pages"] == 1000