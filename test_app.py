import unittest
from server import app

class TestLibraryAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_book(self):
        response = self.app.post('/books', json={"id": 1, "title": "Test Book 1", "author": "Author 1"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()["message"], "Book added successfully")

    def test_get_books(self):
        self.app.post('/books', json={"id": 1, "title": "Test Book 1", "author": "Author 1"})
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_get_single_book(self):
        self.app.post('/books', json={"id": 1, "title": "Test Book 1", "author": "Author 1"})
        response = self.app.get('/books/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["title"], "Test Book 1")

    def test_update_book(self):
        self.app.post('/books', json={"id": 1, "title": "Test Book 1", "author": "Author 1"})
        response = self.app.put('/books/1', json={"title": "Updated Book 1"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["message"], "Book updated successfully")
        updated_response = self.app.get('/books/1')
        self.assertEqual(updated_response.get_json()["title"], "Updated Book 1")

    def test_delete_book(self):
        self.app.post('/books', json={"id": 1, "title": "Test Book 1", "author": "Author 1"})
        response = self.app.delete('/books/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["message"], "Book deleted successfully")
        get_response = self.app.get('/books/1')
        self.assertEqual(get_response.status_code, 404)

    def test_duplicate_book_id(self):
        self.app.post('/books', json={"id": 1, "title": "Test Book 1", "author": "Author 1"})
        response = self.app.post('/books', json={"id": 1, "title": "Duplicate Book", "author": "Author 2"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["error"], "Book with this ID already exists")

    def test_missing_fields_in_book(self):
        response = self.app.post('/books', json={"id": 1, "title": "Test Book 1"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["error"], "Missing required fields: id, title, or author")

    def test_add_member(self):
        response = self.app.post('/members', json={"id": 1, "name": "Member 1"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()["message"], "Member added successfully")

    def test_get_members(self):
        self.app.post('/members', json={"id": 1, "name": "Member 1"})
        response = self.app.get('/members')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_get_single_member(self):
        self.app.post('/members', json={"id": 1, "name": "Member 1"})
        response = self.app.get('/members/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["name"], "Member 1")

    def test_update_member(self):
        self.app.post('/members', json={"id": 1, "name": "Member 1"})
        response = self.app.put('/members/1', json={"name": "Updated Member 1"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["message"], "Member updated successfully")
        updated_response = self.app.get('/members/1')
        self.assertEqual(updated_response.get_json()["name"], "Updated Member 1")

    def test_delete_member(self):
        self.app.post('/members', json={"id": 1, "name": "Member 1"})
        response = self.app.delete('/members/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["message"], "Member deleted successfully")
        get_response = self.app.get('/members/1')
        self.assertEqual(get_response.status_code, 404)

    def test_duplicate_member_id(self):
        self.app.post('/members', json={"id": 1, "name": "Member 1"})
        response = self.app.post('/members', json={"id": 1, "name": "Duplicate Member"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["error"], "Member with this ID already exists")

    def test_missing_fields_in_member(self):
        response = self.app.post('/members', json={"id": 1})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["error"], "Missing required fields: id or name")


if __name__ == '__main__':
    unittest.main()
