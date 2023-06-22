from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['carpooling']
collection = db['bids']

@app.route('/')
def index():
    return render_template('bids.html')

@app.route('/accept_bid', methods=['POST'])
def accept_bid():
    bid_id = request.form['bid_id']

    # Fetch the bid from MongoDB
    bid = collection.find_one({'_id': (bid_id)})

    if bid:
        # Perform necessary operations to accept the bid
        # ...

        return 'Bid accepted!'
    else:
        return 'Bid not found!'

if __name__ == '__main__':
    app.run(debug=True)
