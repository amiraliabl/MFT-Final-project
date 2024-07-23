import csv
import random


def is_BookID_unique(id):
    with open("C:\\Users\\NoteBook\\Documents\\book_management_project\\books.csv") as books:
        content = csv.DictReader(books)
        for row in content:
            if eval(row['id']) == id:
                return False
                break
        else:
            return True
        
        
def generate_BookID():
    random_id = random.randint(102, 602)
    return random_id


class Book:
    @classmethod
    def book(Book, name, author, id):
        Book.name = name
        Book.author = author
        Book.id = id