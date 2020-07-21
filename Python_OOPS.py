'''
Library Implementation through Python OOPS concept
'''

class Library:
    def __init__(self, list_1, name):
        self.booksList = list_1
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
        self.lendDict.pop(book)
        print("Book has been removed from the list")

if __name__ == '__main__' :
    krishna = Library(['Factfulness', 'Sapiens', 'Metamorphsis'],'K-Library')

    while(True):
        print(f"Welcome to the {krishna.name} library, Enter your choice to continue....\n")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")

        user_choice = int(input("Enter your choice...\n=> "))

        if user_choice == 1:
            krishna.displayBooks()

        elif user_choice == 2:
            name = input('Enter the name of the book: ')
            user = input("Enter your name: ")
            krishna.lendBook(user, name)

        elif user_choice == 3:
            book = input("Enter the name of the book: ")
            krishna.addBook(book)
        
        elif user_choice == 4:
            book = input("Enter the name of the book: ")
            krishna.returnBook(book)
        
        else:
            print("Not a valid input...")

        print('Press Q to Quit or C. to Continue...')
        user_choice = ''
        while(user_choice!= 'C' and user_choice != 'Q'):
            user_choice = input()
            if user_choice == 'Q':
                exit()
            else:
                continue
