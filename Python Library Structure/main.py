# main.py
# 
# main program to test Library, Book, and person objects and their methods

import person as p
import book as b
import library as l

try:
    hopCatalog = open("catalog.csv", "r")
except:
    print('Error; "catalog.csv" was not found.')
    exit(1)

lib = p.Person("Eric", "Hopkins", 'male')
l1 = l.Library("Hopkins Personal Library", hopCatalog, lib)
hopCatalog.close()

p1 = p.Person("Ethan", "Sevedge", 'male')
p2 = p.Person("Jack", "Benny", 'male')
p3 = p.Person("Boudica", "", 'female')
p4 = p.Person("Ulysses", "", 'male')

people = [lib, p1, p2, p3, p4]

b1 = l1.findBook('Sense and Sensibility')
b2 = l1.findBook('Wardrobe')
b3 = l1.findBook('Where the Sidewalk Ends')
b4 = l1.findBook('Fitzgerald')
b5 = l1.findBook("Emily Bronte")
b6 = l1.findBook("Shakespeare")
b7 = l1.findBook("Homer")
b8 = l1.findBook("Age of Myth")
b9 = l1.findBook("Dragon Tattoo")
b10 = l1.findBook("1984")
b11 = l1.findBook("451")
b12 = l1.findBook("Holes")

books = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12]

print(f'{l1.name} successfully instantiated.')
print("")
for person in people:
    print(f'{person.getName()} successfully instantiated.')
print("")
for bk in books:
    print(f'{bk.title} successfully instantiated.')
print("")

print("Library catalog: ")
l1.printCatalog()
print("")

# Ethan checks out books
l1.checkout(b1, p1)
l1.checkout(b2, p1)
l1.checkout(b3, p1)
print("")

# Jack checks out books
l1.checkout(b4, p2)
l1.checkout(b5, p2)
l1.checkout(b6, p2)
print("")

# Ethan turns in books
l1.turnIn(b1, p1)
l1.turnIn(b2, p1)
l1.turnIn(b3, p1)
print("")

# Boudica checks out books
l1.checkout(b.Book("Out of the Silent Planet", "C.S. Lewis"), p3)
l1.checkout(b3, p3)
l1.checkout(b7, p3)
l1.checkout(b8, p3)
print("")

# Ulysses checks out books
l1.checkout(b8, p4)
l1.checkout(b9, p4)
l1.checkout(b10, p4)
l1.checkout(b11, p4)
print("")

print("Current available books: ")
l1.printAvailable()
print("")

print("Curent unavailable books: ")
l1.printUnavailable()
print("")

l1 + b.Book("Out of the Silent Planet", "C.S. Lewis")
l1 - b.Book("Divergent", "Veronica Roth")
l1 + b.Book("1984", "George Orwell")
l1 - b4
print("")

# Jack turns in books
l1.turnIn(b4, p2)
l1.turnIn(b5, p2)
l1.turnIn(b6, p2)
print("")

# Boudica turns in books
l1.turnIn(b6, p3)
l1.turnIn(b3, p3)
l1.turnIn(b7, p3)
l1.turnIn(b8, p3)
print("")

# Ulysses turns in books
l1.turnIn(b9, p4)
l1.turnIn(b10, p4)
l1.turnIn(b11, p4)
l1.turnIn(b12, p4)
print("")

l1.checkout(l1.catalog[0], p.Person("Howdy", "Doody", "male"))

l1.outputCatalog("hopCatalog.csv")
print("")

try:
    hopCatalog = open("hopCatalog.csv", "r")
except:
    print('Error; "hopCatalog.csv" was not found.')
    exit(1)

l2 = l.Library("Hopkins New Personal Library", hopCatalog, lib)
hopCatalog.close()
print(f'{l2.name} successfully instantiated.')
print("")
print("Library catalog: ")
l1.printCatalog()
