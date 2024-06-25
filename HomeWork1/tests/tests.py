import pytest

from HomeWork1.classes import Book, Library, LibraryItem


@pytest.fixture(scope="function")
def book_instance():
    return Book("Book", "Author", 2000, True, 'good')


@pytest.fixture(scope="function")
def not_borrowed_book_instance():
    return Book("Book2", "Author", 1000, False, 'good')


@pytest.fixture(scope="function")
def lib_instance():
    return Library([])


def test_wrong_book_year() -> None:
    with pytest.raises(ValueError, match="Invalid year of the book"):
        Book("Book Name", "Autor", -1000, False, 'good')


def test_correct_book_year() -> None:
    Book("Book Name", "Autor", 1000, False, 'good')


def test_check_if_item_in_library(lib_instance: "Library", book_instance) -> None:
    lib_instance.add_item(book_instance)
    assert lib_instance.check_if_item_in_library(book_instance) == True


def test_add_unexisting_book(book_instance: "Book", lib_instance: "Library") -> None:
    lib_instance.add_item(book_instance)
    assert lib_instance.check_if_item_in_library(book_instance)


def test_add_existing_book(book_instance: "Book", lib_instance: "Library") -> None:
    with pytest.raises(AttributeError, match=f"Item {book_instance.title}, already in Library"):
        lib_instance.add_item(book_instance)
        lib_instance.add_item(book_instance)


def test_remove_presented_item(book_instance: "Book", lib_instance: "Library") -> None:
    lib_instance.add_item(book_instance)
    lib_instance.remove_item(book_instance)
    assert not lib_instance.check_if_item_in_library(book_instance)  # Check if book not in Library


def test_remove_unpresented_item(book_instance: "Book", lib_instance: "Library") -> None:
    with pytest.raises(AttributeError, match=f"Item {book_instance.title}, is not present in Library!"):
        lib_instance.remove_item(book_instance)


def test_borrow_borrowed_book(book_instance: "Book", lib_instance: "Library") -> None:
    with pytest.raises(AttributeError, match=f"Book {book_instance.title} is already borrowed!"):
        lib_instance.add_item(book_instance)
        lib_instance.borrow_book(book_instance)


def test_borrow_unpresented_book(book_instance: "Book", lib_instance: "Library") -> None:
    with pytest.raises(AttributeError, match=f"Item {book_instance.title}, is not present in Library!"):
        lib_instance.borrow_book(book_instance)


def test_borrow_not_borrowed_book(not_borrowed_book_instance: "Book", lib_instance: "Library") -> None:
    lib_instance.add_item(not_borrowed_book_instance)
    assert not lib_instance.check_if_book_borrowed(not_borrowed_book_instance)
    lib_instance.borrow_book(not_borrowed_book_instance)
    assert lib_instance.check_if_book_borrowed(not_borrowed_book_instance)


def test_return_not_borrowed_book(not_borrowed_book_instance: "Book", lib_instance: "Library") -> None:
    with pytest.raises(AttributeError, match=f"Book {not_borrowed_book_instance.title}  is not borrowed!"):
        lib_instance.add_item(not_borrowed_book_instance)
        lib_instance.return_book(not_borrowed_book_instance)


def test_return_unpresented_book(book_instance: "Book", lib_instance: "Library") -> None:
    with pytest.raises(AttributeError, match=f"Item {book_instance.title}, is not present in Library!"):
        lib_instance.return_book(book_instance)


def test_return_borrowed_book(book_instance: "Book", lib_instance: "Library") -> None:
    lib_instance.add_item(book_instance)
    assert lib_instance.check_if_book_borrowed(book_instance)
    lib_instance.return_book(book_instance)
    assert not lib_instance.check_if_book_borrowed(book_instance)
