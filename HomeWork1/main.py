from HomeWork1.Classes import Book, Library, LibraryItem

if __name__ == '__main__':
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
