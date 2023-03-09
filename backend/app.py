from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from chat import bot

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Create an SQLite DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Add Database via MySQl on Local Machine
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:3X47Qy!b@projectkarty.cmoarzscfdhk.eu-west-2.rds' \
                                        '.amazonaws.com/conversations'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Secret Key
app.config['SECRET_KEY'] = "No one knows what it is"

# Initialize the Database
db = SQLAlchemy(app)


@app.route("/")
@cross_origin()
def home():
    return "Hello!!!!"


@app.route("/getReply", methods=['POST'])
@cross_origin()
def get_response():
    req_data = request.get_json()
    print(req_data)
    temp = req_data['temp']
    print(temp)
    message = temp['msg']
    print(message)
    botResponse = bot.get_response(message)
    return str(botResponse)


if __name__ == "__main__":
    app.run()
