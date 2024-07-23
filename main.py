from member import Member
from tools import ClearTerminal, Wait, ColoredNotification, add_line
from admin import Admin


def main():
    print(ColoredNotification('hi welcom to the library managment system!','red'))
    add_line()
    role = input(ColoredNotification("if you are a member enter 1 and if you are a admin enter 2 : ", 'blue'))
    if role.lower() == '1':
        register_or_login = input(ColoredNotification("if you have an account please enter '1' and if you have to creat an account enter '2' : ", 'green'))
        if register_or_login.lower() == '1':
            Member.login()
            ClearTerminal()
            print(ColoredNotification('welcom to your account!!!', 'red'))
            add_line()
            member_panel = True 
            while member_panel:
                user_request = input(ColoredNotification(' what do you want to do?\n1 search book,2 borrow book,3 see the list of book,4 exit\nenter the number please! :', 'blue'))
                if user_request == '1':
                    Member.searchBook()
                    Wait()
                elif user_request == '2':
                    Member.borrowBook()
                    Wait()
                elif user_request == '3':
                    Member.listOfbook()
                    Wait()
                elif user_request == '4':
                    member_panel = False
                    print(ColoredNotification('good luck!!!', 'red'))
                else:
                    print(ColoredNotification('please enter a valid input!!!', 'red'))
                    Wait()
        elif register_or_login.lower() == '2':
            Member.register_member()
            new_member_request = input(ColoredNotification('if you want to login to your account enter 1 and if you want exit enter 2 : ','red'))
            if new_member_request == '1':
                Member.login()
                ClearTerminal()
                print(ColoredNotification('welcom to your account!!!', 'red'))
                add_line()
                member_panel = True 
                while member_panel:
                    user_request = input(ColoredNotification(' what do you want to do?\n1 search book,2 borrow book,3 see the list of book,4 exit\nenter the number please! :', 'blue'))
                    if user_request == '1':
                        Member.searchBook()
                        Wait()
                    elif user_request == '2':
                        Member.borrowBook()
                        Wait()
                    elif user_request == '3':
                        Member.listOfbook()
                        Wait()
                    elif user_request == '4':
                        member_panel = False
                        print(ColoredNotification('good luck!!!', 'red'))
                    else:
                        print(ColoredNotification('please enter a valid input!!!', 'red'))
                        Wait()
            elif new_member_request == '2':
                print(ColoredNotification('good luck!', 'red'))
            else:
                print(ColoredNotification('please enter a valild input', 'red'))          
        else:
            print(ColoredNotification('please enter a valid input!!!', 'red'))
    elif role.lower() == '2':
        Admin.login()   
        ClearTerminal()
        print(ColoredNotification('welcom to your account!!!', 'red'))
        add_line()
        admin_panel = True
        while admin_panel:
            admin_request = input(ColoredNotification('what do you want to do?\n1 add book,2 remove book,3 see list of book,4 search book,5 see borrow list,6 see member list,7 exit\nenter the number please! : ', 'green'))     
            if admin_request == '1':
                Admin.addBook()
                Wait()
                add_line()
            elif admin_request == '2':
                Admin.removeBook()
                Wait()
                add_line()
            elif admin_request == '3':
                Admin.listOfbook()
                Wait()
                add_line()
            elif admin_request == '4':
                Admin.searchBook()
                Wait()
                add_line()
            elif admin_request == '5':
                Admin.borrowList()
                Wait()
                add_line()
            elif admin_request == '6':
                Admin.memberList()
                Wait()
                add_line()
            elif admin_request == '7':
                admin_panel = False
                add_line()
                print(ColoredNotification('good luck!!!', 'red'))
            else:
                ClearTerminal()
                print(ColoredNotification('please enter valid input!!!', 'red'))
                add_line()
                Wait()

                                              
if __name__ == '__main__':
    main()
    