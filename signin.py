
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['carpooling']
collection = db['users']

@app.route('/')
def index():
    return render_template('sign in.html')

@app.route('/sign in', methods=['POST'])
def signin():
    email = request.form['email']
    password = request.form['password']

    # Save the data to MongoDB
    user_data = {
        'email': email,
        'password': password
    }
    collection.insert_one(user_data)

    return 'Sign-in Successful!'

if __name__ == '__main__':
    app.run(debug=True)
