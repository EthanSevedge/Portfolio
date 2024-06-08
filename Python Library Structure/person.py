# person.py
# 
# defines a Person object with a first name, last name, and list of books checked out from some Library object
# also defines methods relating to said Person

class Person:
    def __init__(self, fName, lName, gender):
        if not (gender.lower() == 'male' or gender.lower() == 'female'):
            raise ValueError('Gender parameter must be "male" or "female".')
        self.fName = fName
        self.lName = lName
        self.gender = gender.lower()
        self.subPro = "he" if self.gender == "male" else "she"
        self.cSubPro = self.subPro[0].upper() + self.subPro[1:]
        self.possPro = "his" if self.gender == "male" else "her"
        self.cPossPro = self.possPro[0].upper() + self.possPro[1:]
        self.dirObjPro = "him" if self.gender == "male" else "her"
        self.currentBooks = []
    
    def __repr__(self):
        return f'Person: name = "{self.fName} {self.lName}"; currentBooks = {self.formattedBookList()}'
        
    # returns how many Books are checked out by a Person
    def __len__(self):
        return len(self.currentBooks)
    
    # returns a list of "book-strings" formatted according to "{book.title}" by {book.author}
    def formattedBookList(self):
        formattedBooks = []
        for book in self.currentBooks:
            formattedBooks.append(book.formattedTitleAuthor())
        return formattedBooks
    
    def getName(self):
        if not self.lName == "":
            return f"{self.fName} {self.lName}"
        else:
            return self.fName
    
    # prints name of Person
    def printName(self):
        print(self.getName())
    
    # prints Books checked out by Person in formatted form, one book per line
    def printCurrentBooks(self):
        for bkStr in self.formattedBookList():
            print(bkStr)
