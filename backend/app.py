from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQL@1234",
    database="freelancer_marketplace"
)

@app.route('/')
def home():
    return "Welcome to the Freelancer Marketplace!"


@app.route('/jobs', methods=['GET'])
def get_jobs():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Jobs;")
    jobs = cursor.fetchall()
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
