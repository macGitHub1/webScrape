#imports
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config ['MONGO_DBNAME'] = 'surf_db'
mongo = PyMongo(app)


@app.route("/")
def home():
    # Find data
    surfList = mongo.db.items.find()
    return render_template("index.html", surfList=surfList)
    




if __name__ == "__main__":
    app.run(debug=True)

