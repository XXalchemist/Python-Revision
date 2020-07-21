'''
Library Implementation through Python OOPS concept
'''

class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}
    
    def displayBooks(self):
        print( f"We have following books in library: {self.name}" )
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book : user})
            print("Database updated .... You can take your book now !!!")
        else:
            print( f"Sorry ! This book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the list")

    def returnBook(self, book):
        self.booksList.remove(book)
        print("Book has been removed from the list")

if __name__ == '__main__' :
    library_A = Library()
