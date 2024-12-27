from flask import Flask, request, jsonify

app = Flask(__name__)

books = []
members = []

def find_item_by_id(items, item_id):
    return next((item for item in items if item['id'] == item_id), None)

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data.get('id') or not data.get('title') or not data.get('author'):
        return jsonify({"error": "Missing required fields: id, title, or author"}), 400
    
    if find_item_by_id(books, data['id']):
        return jsonify({"error": "Book with this ID already exists"}), 400
    
    books.append(data)
    return jsonify({"message": "Book added successfully"}), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = find_item_by_id(books, book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book), 200

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = find_item_by_id(books, book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    
    data = request.get_json()
    book.update(data)
    return jsonify({"message": "Book updated successfully"}), 200

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = find_item_by_id(books, book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    
    books.remove(book)
    return jsonify({"message": "Book deleted successfully"}), 200


@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(members), 200

@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    if not data.get('id') or not data.get('name'):
        return jsonify({"error": "Missing required fields: id or name"}), 400
    
    if find_item_by_id(members, data['id']):
        return jsonify({"error": "Member with this ID already exists"}), 400
    
    members.append(data)
    return jsonify({"message": "Member added successfully"}), 201

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = find_item_by_id(members, member_id)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    return jsonify(member), 200

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    member = find_item_by_id(members, member_id)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    
    data = request.get_json()
    member.update(data)
    return jsonify({"message": "Member updated successfully"}), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = find_item_by_id(members, member_id)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    
    members.remove(member)
    return jsonify({"message": "Member deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)

