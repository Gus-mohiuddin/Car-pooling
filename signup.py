from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['carpooling']
collection = db['users']

@app.route('/')
def index():
    return render_template('sign up.html')

@app.route('/sign up', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    # Save the data to MongoDB
    user_data = {
        'name': name,
        'email': email,
        'password': password
    }
    collection.insert_one(user_data)

    return 'Sign-up Successful!'

if __name__ == '__main__':
    app.run(debug=True)
