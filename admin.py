import csv
import pandas as pd
from book import generate_BookID, is_BookID_unique, Book
from tools import ColoredNotification, add_line


class Admin:
    def __init__(self, name, email, passwrod):
        self.name = name
        self.email = email
        self.__password = passwrod
        
    def addBook():
        Book.name = input(ColoredNotification('please enter the name of book : ', 'blue'))
        Book.author = input(ColoredNotification('please enter the name of the author : ', 'blue'))
        Id = generate_BookID()
        while not is_BookID_unique(Id):
            Id = generate_BookID()
        Book.id = Id
        with open("books.csv", 'a') as books:
            csv_write = csv.writer(books)
            csv_write.writerow([Book.name,Book.author,Book.id])
            add_line()
        print(ColoredNotification(f"The book was successfully added!\nThe book id is : {Book.id},", 'red'))
    
    def removeBook():
        Book.id = input(ColoredNotification('please enter id of the book that you want to remove : ','blue'))
        with open("books.csv") as books:
            csv_reader = csv.DictReader(books)
            list_of_id = [row["id"] for row in csv_reader]
            lineCounter = 0
            for item in list_of_id[::-1]:
                lineCounter -= 1
                if item == Book.id:
                    break
        content = pd.read_csv("books.csv")
        content = content.drop(content.index[lineCounter])  # remove the row that we want
        content.to_csv("books.csv", index=False)
        add_line()
        print(ColoredNotification("book was successfully removed!", 'blue'))
    
    def searchBook():
        Book.id = input(ColoredNotification('please enter the id of book : ', 'blue'))
        with open("books.csv") as books:
            content = csv.DictReader(books)
            for row in content:
                if row['id'] == Book.id:
                    add_line()
                    print(ColoredNotification(f"Book ID :{row['id']}| Book name : {row['name']}| Book author : {row['author']}", 'green'))
                    break
            else:
                add_line()
                print(ColoredNotification('book was not found!', 'red'))
    
    def borrowList():
        with open("list_of_borrow.csv") as borrowList:
            borrowListReader = csv.DictReader(borrowList)
            line_counter = 0
            for row in borrowListReader:
                line_counter += 1
                print(ColoredNotification(f"{line_counter}|name of member:{row['nameOfMember']}|ID of member:{row['IDOfMember']}|ID of book:{row['IDofBook']}", 'green'))
                
    def memberList():
        with open("members.csv") as members:
            content = csv.DictReader(members)
            line_counter = 0
            for row in content:
                line_counter += 1
                print(ColoredNotification(f"{line_counter}| name:{row['name']}|email:{row['email']}|ID:{row['id']}",'green'))
                
    def listOfbook():
        with open("books.csv") as books:
            content = csv.DictReader(books)
            line_counter = 0
            for row in content:
                line_counter += 1
                print(ColoredNotification(f"{line_counter}| name:{row['name']}|author:{row['author']}|ID:{row['id']}", 'green'))
                
    @classmethod
    def login(Admin):
        email = input('please enter your email : ')
        password = input('please enter your password : ')
        with open("admins.csv") as listOfAdmin:
            admins = csv.DictReader(listOfAdmin)
            for row in admins:
                if row['email'] == email and row['password'] == password:
                    return Admin(row['name'], email, password)
                    break
            else:
                raise ValueError(ColoredNotification('your email or password was incorrect', 'red'))
    
    
    
            
