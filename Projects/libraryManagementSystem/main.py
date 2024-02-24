class Book:

    def __int__(self, book_id, book_title, book_author, copies):
        self.book_id = book_id
        self.book_title = book_title
        self.book_author = book_author
        self.copies = copies

    def __str__(self):
        return f"\nBook Title: {self.book_title}\n Book Author: {self.book_author}\n Available Copies: {self.copies}"

    def checkIn(self):
        self.copies += self.copies

    def checkOut(self):
        self.copies -= self.copies


class LibraryMember(Book):
    def __init__(self, book_id, book_title, book_author, member_id, member_name):
        super().__int__(book_id, book_title, book_author)
        self.member_id = member_id
        self.member_name = member_name

    def __str__(self):
        return f"Member Name: {self.member_name}"

    def checkOut_book(self ):





