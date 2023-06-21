from flask import Flask, render_template, request

app = Flask(__name__)

# Render the HTML form
@app.route('/')
def home():
    ride_id = get_ride_id()  # Replace this with your logic to obtain the ride ID from the backend
    return render_template('bidride.html', ride_id=ride_id)

# Handle POST request to /bids
@app.route('/bids', methods=['POST'])
def raise_bid():
    passenger_name = request.form['passenger-name']
    bid_amount = request.form['bid-amount']
    ride_id = request.form['ride-id']

    # Here, you can process the form data and save the bid to a database or perform any other necessary actions.
    # You can access the form field values using the 'passenger_name', 'bid_amount', and 'ride_id' variables.

    return 'Bid raised successfully!'  # Return a response to the client

def get_ride_id():
    # Replace this function with your logic to obtain the ride ID from the backend
    # You can fetch the ride ID from a database, generate it dynamically, or retrieve it from another source
    return '12345'  # Replace '12345' with the actual ride ID

if __name__ == '__main__':
    app.run(debug=True)
