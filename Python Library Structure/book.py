# book.py
# 
# 

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = True
        self.prevBorrowers = []
        self.currentBorrower = None
    
    # returns an f-string with all relevant information about the book
    # Note: for currentBorrower, I ended up using chr(34) to represent quotes because f-strings disallow the use of escaped characters
    def __repr__(self):
        return f'Book: title = "{self.title}"; author = "{self.author}"; status = {"available" if self.status else "checked out"}; previousBorrowers = {self.getPrevBorrowersNames()}; currentBorrower = {"None" if (self.currentBorrower is None) else (chr(34) + self.currentBorrower.getName() + chr(34)) }'
        
    def __len__(self):
        return len(self.prevBorrowers)
        
    def __eq__(self, other):
        if isinstance(other, Book):
            return ((self.title == other.title) and (self.author == other.author))
        else:
            return False
            
    def formattedTitleAuthor(self):
        return f'"{self.title}" by {self.author}'
        
    def printName(self):
        print(self.formattedTitleAuthor())
        
    def printStatus(self):
        print(("Available" if self.status else f"Checked out by {self.currentBorrower.getName()}"))
        
    def getPrevBorrowersNames(self):
        names = []
        for person in self.prevBorrowers:
            names.append(person.getName())
        return names
    
    def printPrevBorrowers(self):
        for name in self.getPrevBorrowersNames():
            print(name)
            
    
    
    
