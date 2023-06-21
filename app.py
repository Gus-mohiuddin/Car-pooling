from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['carpooling_db']
bids_collection = db['bids']
@app.route('/')
def home():
    return render_template('driver.html')

# Handle POST request to /rides
@app.route('/rides', methods=['POST'])
def create_ride():
    source = request.form['source']
    destination = request.form['destination']
    date = request.form['date']
    seats = request.form['seats']

    # Here, you can process the form data and save it to a database or perform any other necessary actions.
    # You can access the form field values using the 'source', 'destination', 'date', and 'seats' variables.

    return 'Ride created successfully!' 


@app.route('/bidride', methods=['POST'])
def raise_bid():
    passenger_name = request.form['passenger-name']
    bid_amount = request.form['bid-amount']
    ride_id = request.form['ride-id']
    
    bid = {
        'passenger_name': passenger_name,
        'bid_amount': bid_amount,
        'ride_id': ride_id
    }
    
    # Save the bid to MongoDB
    bid_id = bids_collection.insert_one(bid).inserted_id
    
    # Redirect back to the Bid Ride Page or any other desired page
    return redirect('/bidride')

if __name__ == '__main__':
    app.run(debug=True)



   