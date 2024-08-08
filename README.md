# Library Management System

## Overview

This project is a simple Library Management System built with Django and Django REST Framework (DRF). It provides basic functionalities for user authentication, book listing, borrowing, and returning books. It uses JSON Web Tokens (JWT) for user authentication and includes endpoints for user signup, login, book retrieval, borrowing, and returning books.

## Features

- **User Authentication:**
  - Signup: Register new users.
  - Login: Authenticate users and provide JWT tokens for access.

- **Book Management:**
  - List Books: Retrieve a list of all available books.

- **Borrowing System:**
  - Borrow Book: Allow authenticated users to borrow books if they are available.
  - Return Book: Allow authenticated users to return borrowed books.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/theycallmejoly/library-management-system.git
   cd library-management-system
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for accessing Django admin):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Endpoints

- **POST** `/api/signup/`  
  Registers a new user. Expects JSON with `username`, `email`, and `password`.

- **POST** `/api/login/`  
  Authenticates a user and returns JWT tokens. Expects JSON with `username` and `password`.

- **GET** `/api/books/`  
  Retrieves a list of all books. Requires authentication.

- **POST** `/api/borrow/`  
  Allows a user to borrow a book. Expects JSON with `book` ID. Requires authentication.

- **POST** `/api/return/<int:pk>/`  
  Allows a user to return a borrowed book. Expects the primary key (`pk`) of the borrow record. Requires authentication.

## Models

- **Book**: Represents a book with fields for title, author, and availability.

- **Borrow**: Represents a borrowing record with fields for user, book, borrowed date, and return date.

## Serializers

- **UserSerializer**: Serializes user data for registration and authentication.

- **BookSerializer**: Serializes book data for listing and interaction.

- **BorrowSerializer**: Serializes borrowing records for creating and updating.

## Authentication

The project uses JWT for authentication. After logging in, the user receives a `refresh` token and an `access` token. The `access` token is used to authenticate requests to protected endpoints.

## Permissions

- **AllowAny**: Used for user signup and login.
- **IsAuthenticated**: Used for endpoints that require the user to be logged in, such as viewing books, borrowing, and returning books.

## Contact

For questions or suggestions, please contact [theycallmejoly@gmail.com].
