class LibraryItem:
    def __init__(self, title: str, author: str, publication_year: int) -> None:
        self.verify_publication_year(publication_year)
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self) -> None:
        print(f"Title: {self.title}\n"
              f"Author: {self.author}\n"
              f"Publication Year: {self.publication_year}")

    @classmethod
    def verify_publication_year(cls, year: int) -> None:
        if not year.is_integer() or year < 0 or year > 2024:
            raise ValueError(f"Invalid year of the book")


class Book(LibraryItem):
    def __init__(self, title: str, author: str, publication_year: int,
                 is_borrowed: bool, book_condition: str) -> None:

        super().__init__(title, author, publication_year)
        self.is_borrowed = is_borrowed
        self.book_condition = book_condition

    def display_info(self) -> None:
        super().display_info()
        print(f"Is Book Borrowed? {self.is_borrowed}\n"
              f"Book Condition: {self.book_condition}")


class Library:
    def __init__(self, item_collections: list["LibraryItem"]) -> None:
        self.item_collections = item_collections

    def add_item(self, new_item: LibraryItem) -> None:
        if not self.check_if_item_in_library(new_item):
            print(f"Adding Library Item {new_item.title} to Library")
            self.item_collections.append(new_item)
        else:
            raise AttributeError(f"Item {new_item.title}, already in Library")

    def remove_item(self, item_to_remove: "LibraryItem") -> None:
        if self.check_if_item_in_library(item_to_remove):
            print(f"Removing Library Item {item_to_remove.title} from Library")
            self.item_collections.remove(item_to_remove)
        else:
            raise AttributeError(f"Item {item_to_remove.title}, not present in Library")

    def borrow_book(self, book: "Book") -> None:
        if self.check_if_item_in_library(book):
            if book.is_borrowed == False:
                book.is_borrowed = True
            else:
                raise ValueError(f"Book {book.title}  is not borrowed!")
            print(f"You have borrowed a book {book.title}")
        else:
            raise ValueError(f"Book {book.title} is not present in Library!")

    def return_book(self, book: "Book") -> None:
        if self.check_if_item_in_library(book):
            if book.is_borrowed==True:
                book.is_borrowed = False
                print(f"You returned a book {book.title}")
            else:
                raise ValueError(f"Book {book.title}  is not borrowed!")
        else:
            raise ValueError(f"Book {book.title}  is not present in Library!")

    def display_available_books(self) -> None:
        for item in self.item_collections:
            if hasattr(item, "is_borrowed"):
                if item.is_borrowed == False:
                    print(f"Available Item: {item.title}")

    def check_if_item_in_library(self, item: "LibraryItem") -> bool:
        if item in self.item_collections:
            return True
        else:
            return False



# Creation of objects
book1 = Book("Harry Potter", "Jk", 2001, False, "good")
book2 = Book("Golden Horde", "Mehmement", 1005, True, "bad")
book3 = Book("Clean Code", "Bob Martin", 2012, True, "good")
library_item_1 = LibraryItem("Journal", "Vogue", 2003)
library_item_2 = LibraryItem("Computer", "Hp", 2022)

# Creation of list of all objects to pass to Library class
Library_items_list = [book1, book2, book3, library_item_1, library_item_2]

# Creation of Library class instance and passing our list
library_instance = Library(Library_items_list)

# Created one more book to add to add_item function
book4 = Book("Azbuka", "Life", 2000, False, "good")

# Adding Book object to list
library_instance.add_item(book4)

# Removing Book object from list
library_instance.remove_item(book3)

# Borrowing and returning books and printing available books as result
library_instance.display_available_books()
library_instance.borrow_book(book1)
library_instance.display_available_books()
library_instance.return_book(book2)
library_instance.display_available_books()


# -- Block of the code that shows handling of the passing wrong information and operation --

# book5 = Book("Bad Book", "Devil", 1, False, "good")
# library_instance.remove_item(book5)
# library_instance.add_item(book5)
# # library_instance.return_book(book5)
# book5 = Book("Bad Book2", "Devil", -5, False, "good")
