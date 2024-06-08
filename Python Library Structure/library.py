# library.py
# 
# 

import person as p
import book as b


class Library:
    # __init__
    # Requires catalog to be a file OPEN FOR READING
    # The catalog file has columns author and title
    # Currently this requires the Book class to be defined
    # in a file called book.py (you may change these as desired)
    # and requires the Book class __init__() function to take
    # the title of the book first, author second.
    def __init__(self, name, catalog, librarian = None):
        self.name = name
        self.catalog = []
        self.librarian = librarian
        for line in catalog:
            clean_line = line.strip()
            clean_line = clean_line.split(',')
            if len(clean_line) < 2:
                raise ValueError(f"The catalog file was incorrectly formatted.")
            elif (len(clean_line) == 2):
                clean_line.insert(0, "available")
            elif (len(clean_line) > 3):
                newStr = ""
                for bookStr in clean_line:
                    if bookStr != clean_line[0]:
                        newStr = newStr + bookStr + ","
                clean_line[2] = newStr[:-1]
            book = b.Book(clean_line[2],clean_line[1])
            book.status = False if clean_line[0] == "unavailable" else True
            self.catalog.append(book)
            
    def __repr__(self):
        bookStr = '[\n'
        for book in self.catalog:
            bookStr += f"\t{str(book)},\n"
    #        bookStr += f'{book.formattedTitleAuthor()}, '
    #    bookStr = bookStr[:-2] + "]"
        bookStr += "]"
        return f"Library: name = {self.name}; catalog = {bookStr}"
        
    def __add__(self, book):
        if not isinstance(book, b.Book):
            raise TypeError("The function takes a book object.")
        else:
            for catBook in self.catalog:
                if book == catBook:
                    print(f'Error: "{book.title}" cannot be added to the catalog because it is already in the catalog.')
                    book = None
                    break
            
            if not book is None:
                self.catalog.append(book)
                print(f'{book.formattedTitleAuthor()} successfully added to the catalog.')
        
    def __sub__(self, book):     
        if not isinstance(book, b.Book):
            raise TypeError("The function takes a book object.")
        else:
            inCatalog = False
            for catBook in self.catalog:
                if book == catBook:
                    inCatalog = True
                    book = catBook
                    break
            
            if inCatalog:
                if book.status:
                    self.catalog.remove(book)
                    print(f'{book.formattedTitleAuthor()} successfully removed from the catalog.')
                else:
                    print(f'Error: "{book.title}" cannot be removed from the catalog because it is unavailable.')
            else:
                print(f'Error: "{book.title}" cannot be removed from the catalog because it is not in the catalog.')
    
    def __len__(self):
        return len(self.catalog)
        
    # allows one to search for a book by title or author; returns book if only one match is found, otherwise returns None
    def findBook(self, str):
        matches = []
        for book in self.catalog:
            if (str in book.title) or (str in book.author):
                matches.append(book)
        if len(matches) == 1:
            return matches[0]
        else:
            if len(matches) == 0:
                print(f'"{str}": No matches found')
            else:
                print(f'Matches found for "{str}":')
                for book in matches:
                    print(book)
            return None
    
    def printCatalog(self):
        for book in self.catalog:
            print(f'{book.formattedTitleAuthor()}; {"available" if book.status else "checked out"}')

    def printAvailable(self):
        for book in self.catalog:
            if book.status:
                print(f'{book.formattedTitleAuthor()}')

    def printUnavailable(self):
        for book in self.catalog:
            if not book.status:
                print(f'{book.formattedTitleAuthor()}; checked out by {book.currentBorrower.getName()}')
    
    def checkout(self, book, person):
        if not (isinstance(book, b.Book) and isinstance(person, p.Person)):
            raise TypeError("The function takes one Book object and one Person object as parameters.")
        else:
            # checks to see if book is in the catalog
            inCatalog = False
            for catBook in self.catalog:
                if book == catBook:
                    inCatalog = True
                    book = catBook
                    break
            
            if inCatalog:
                if book.status:
                    book.status = False
                    book.currentBorrower = person
                    person.currentBooks.append(book)
                    print(f'"{book.title}" successfully checked out from {self.name} by {person.getName()}.')
                else:
                    print(f'Error: {person.getName()} cannot check out "{book.title}" because it is unavailable.')
            else:
                print(f'Error: {person.getName()} cannot check out "{book.title}" because it is not in the catalog.')
    
    def turnIn(self, book, person):
        if not (isinstance(book, b.Book) and isinstance(person, p.Person)):
            raise TypeError("The function takes one Book object and one Person object as parameters.")
        else:
            inCatalog = False
            for catBook in self.catalog:
                if book == catBook:
                    inCatalog = True
                    book = catBook
                    break
            
            if not inCatalog:
                print(f'Error: {person.getName()} cannot check out "{book.title}" because it is not in the catalog.')
            else:
                if book.currentBorrower == person:
                    book.status = True
                    book.prevBorrowers.append(book.currentBorrower)
                    book.currentBorrower = None
                    person.currentBooks.remove(book)
                    print(f'"{book.title}" successfully turned in to {self.name} by {person.getName()}.')
                else:
                    print(f'Error: {person.getName()} did not check out "{book.title}," so {person.subPro} may not return it.')
                    
    def outputCatalog(self, title):
        if not isinstance(title, str):
            raise TypeError("A string argument is required for the function.")
        else:
            try:
                outFile = open(title, "w")
            except:
                raise IOException(f'"{title}" could not be opened')
            newLine = "\n"
            for i in range(len(self.catalog)):
                book = self.catalog[i]
                outFile.write(f'{"available" if book.status else "unavailable"},{book.author},{book.title}{newLine if not (i-1 == len(self.catalog)) else ""}')
            outFile.close()
            print(f"The catalog of {self.name} was outputted successfully.")
