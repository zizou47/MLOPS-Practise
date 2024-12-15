from flask import Flask, jsonify, request

app = Flask(__name__)

# create data

items = [
    {"id": 1, "name": "item1", "description": "this is item1"},
    {"id": 2, "name": "item2", "description": "this is item2"}
]

@app.route('/')
def home():
    return "Welcome to the API"

# get retrieve all items

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


# get  specefiec retrieve all items

@app.route('/items/<int:item_id>', methods = ['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return 'this item does not exist', 404
    return jsonify(item)

# post create new item
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or "name" not in request.json:  # if req not in json format (just random condition)
        return 'this item does not exist', 404
    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,  # access last item if exist then +1 for it else 1 as the first item
        "name": request.json['name'],
        "description": request.json['description']
    }

    items.append(new_item)
    return jsonify(new_item)


# put updating an existing item

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id))
    if item is None:
        return 'this item does not exist', 404
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)
if __name__ == '__main__':
    app.run(debug = True)