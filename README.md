How to Run the Project

Prerequisites
Python 3.10+
pip (Python package manager)


Steps to Run
Clone the repository:

bash
Copy code
git clone https://github.com/YourUsername/YourRepositoryName.git
cd YourRepositoryName
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows

Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
The app will start at http://127.0.0.1:5000.

Run tests:

bash
Copy code
python -m unittest test_app.py


Design Choices

1. Modular Code Structure
Code is organized with reusable functions like find_item_by_id for better readability and maintainability.

3. Stateless Token-Based Authentication
JWT-based authentication ensures secure access to the API endpoints.
Tokens are generated during login and validated for subsequent requests.

5. Pagination and Search
Pagination: Helps manage large datasets by limiting the number of records returned in a single request.
Search: Allows querying books by title or author for user convenience.

7. RESTful Principles
Each endpoint follows RESTful design:
GET: Retrieve resources.
POST: Create new resources.
PUT: Update existing resources.
DELETE: Remove resources.
Assumptions and Limitations

Assumptions
Books and members are uniquely identified by their id fields.
The id field is required and should be manually provided by the user when adding books or members.
Search is case-sensitive and matches exact substrings.
Tokens have a default expiration of 1 hour.


Limitations

No database integration: Data is stored in-memory, so it resets every time the app restarts.
No external libraries: Token handling and search functionality are implemented using standard libraries only, per assignment constraints.
Scalability: The current implementation is suitable for small-scale use but would require a database and caching system for production.


Endpoints


Books

Method	Endpoint	Description
GET	/books	List all books.
GET	/books/<book_id>	Retrieve a specific book.
POST	/books	Add a new book.
PUT	/books/<book_id>	Update a specific book.
DELETE	/books/<book_id>	Delete a specific book.


Members

Method	Endpoint	Description
GET	/members	List all members.
GET	/members/<member_id>	Retrieve a specific member.
POST	/members	Add a new member.
PUT	/members/<member_id>	Update a specific member.
DELETE	/members/<member_id>	Delete a specific member.


Future Enhancements

Database Integration: Use SQLite or PostgreSQL for persistent storage.
Enhanced Authentication: Include user roles and permissions.
Deployment: Host the API on a cloud platform like AWS or Heroku.
