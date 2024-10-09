class Book:

    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    #DOUBLE UNDERSCORE PROPERTIES
    __booklist = None
    
    def set_title(self, newtitle):
        self.title = newtitle

    #CREATE CLASS METHOD
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES
    
    #CREATE STATIC METHOD
    def getBookList():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist


    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

#ACCESS THE CLASS ATTRIBUTE
print("Book types: ", Book.get_book_types())


#create some book instances
b1 = Book("Title1", "HARDCOVER")
b2 = Book("Title1", "PAPERBACK")

#use the static method to access a single object
thebooks = Book.getBookList()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)