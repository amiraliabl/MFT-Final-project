from book import Book
import csv
from random import randint
from tools import ClearTerminal
from tools import ColoredNotification
from tools import add_line


def capacity():
    with open("members.csv") as members:
        content = csv.DictReader(members)
        member_counter = 0
        for row in content:
            member_counter += 1
        if member_counter > 100:
            return False
        else:
            return True


def generate_MemberID():
    random_id = randint(1, 101)
    return random_id


def is_memberID_unique(id):
    with open("members.csv") as members:
        content = csv.DictReader(members)
        for row in content:
            if eval(row['id']) == id:
                return False
                break
        else:
            return True


class Member:
    @classmethod
    def __init__(member, name, email, password, Id):
        member.name = name
        member.email = email
        member.__password = password
        member.Id = Id
    
    @classmethod
    def borrowBook(Member):
        ClearTerminal()
        Book.id = input(ColoredNotification('please enter the id of book that you want to borrow', 'green'))
        with open("books.csv") as books:
            content = csv.DictReader(books)
            for row in content:
                if row['id'] == Book.id.lower():
                    with open("list_of_borrow.csv", 'a') as borrow_list:
                        csv_writer = csv.writer(borrow_list)
                        csv_writer.writerow([Member.name,Member.Id,Book.id])
                        print(ColoredNotification('you have successfully borrowed this book!','red'))
                        break
            else:
                print(ColoredNotification('book was not found!', 'red'))
                
    def searchBook():
        ClearTerminal()
        Book.id = input(ColoredNotification('please enter the id of book', 'blue'))
        with open("books.csv") as books:
            content = csv.DictReader(books)
            for row in content:
                if row['id'] == Book.id:
                    print(ColoredNotification(f"Book ID :{row['id']}| Book name : {row['name']}| Book author : {row['author']}", 'green'))
                    break
            else:
                print(ColoredNotification('Book not found!', 'red'))
                
    def listOfbook():
        ClearTerminal()
        with open("books.csv") as books:
            content = csv.DictReader(books)
            line_counter = 0
            for row in content:
                line_counter += 1
                print(ColoredNotification(f"{line_counter}| name:{row['name']}|author:{row['author']}|ID:{row['id']}", 'green'))
    
    @ classmethod
    def login(Member):
        email = input(ColoredNotification('please enter your email : ', 'green'))
        password = input(ColoredNotification('please enter your password : ', 'green'))
        with open("members.csv") as members:
            content = csv.DictReader(members)
            for row in content:
                if row['email'] == email.lower() and row['password'] == password.lower():             
                    return Member(row['name'], email, password, row['id'])
                    break
            else:
                raise ValueError('your email or password was incorrect')
    
    @classmethod
    def register_member(member):
        if capacity:
            name = input(ColoredNotification('please enter your name : ', 'blue'))
            email = input(ColoredNotification('please enter your email : ', 'red'))
            password = input(ColoredNotification('please enter your password : ', 'green'))
            member_id = generate_MemberID()
            while not is_memberID_unique(member_id):
                member_id = generate_MemberID()
            with open("members.csv", 'a') as members:
                csv_writer = csv.writer(members)
                csv_writer.writerow([name,email,password,member_id])
            add_line()
            print(ColoredNotification('you have been successfully loggedin!!!', 'red'))       
        else:
            print(ColoredNotification('sorry, we are at full capacity.', 'red'))
                

                      