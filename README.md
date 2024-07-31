# Library Management System

Welcome to the Library Management System! This project is a simple implementation of a library management system using Python. It allows members to search, borrow, and enables admins to manage the book catalog.

## Features

- Member registration and login
- Search for books
- Borrow books
- Admin management of books (add, remove, list)
- Data stored in CSV files

## Project Structure

- `main.py`: The main entry point of the application. Handles user interactions and role-based functionality.
- `member.py`: Contains the `Member` class and related functionalities.
- `admin.py`: Contains the `Admin` class and related functionalities.
- `book.py`: Contains the `Book` class and helper functions for book ID management.
- `tools.py`: Utility functions for terminal operations and notifications.

## Setup

1. **Clone the repository**:
      ```bash
   git clone https://github.com/amiraliabl/library-management-system.git
   cd library-management-system

2. Install dependencies:
   Ensure you have Python installed. If not, download and install it [here](https://www.python.org/downloads/).

3. run the application:
   python main.py
   
## Usage
1. **Run the apllication:**

   ``` bash
      python main.py
      

3. **select your role:**
      *  enter '1' for Member
      *  enter '2' for Admin

4. **Member option**
   * register or login to your account
   * Search for books
   * Borrow books
   * List borrowed books

5. **Admin option**
      * Add book to the catalog
      * Remove books from the catalog
      * List all books
      * View borrowed books
      * View member list

## CSV File Path
Ensure the following CSV files are present in the project directory:
- `members.csv:` Stores member details.
- `books.csv:` Stores book details
- `admins.csv`: Stores admin details.
- ` list_of_borrow`: Stores borrow records.

## licence 
This project is licensed under the MIT License.

     
 ## Contributing
 Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.

 ## contact
 If you have any questions or suggestions, feel free to reach out to me at [my email](amiraliabolhassani@gmail.com)

     

