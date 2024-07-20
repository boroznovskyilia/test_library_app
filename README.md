# Library Management System

A simple library management system for managing books using JSON file storage. This project demonstrates how to implement a basic library service with add, get, search, update, and delete operations.


## Prerequisites

- Python 3.10 or later
- `pip` package manager

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/boroznovskyilia/test_library_app.git
    cd test_library_app
    ```

2. **Create a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**

    ```sh
    python3 main.py
    ```

    Follow the on-screen prompts to interact with the library system.


## Running Tests
- Add Book: Add a new book to the library.(Add only unique book. Unique book is detected by similar title author and year)
- Get All Books: Retrieve a list of all books in the library.
- Search Book by Field: Search for a book by title, author, or year.
- Change Book Status: Update the status of a book (e.g., available, issued).
- Delete Book: Remove a book from the library.
