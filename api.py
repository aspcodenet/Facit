import json
from json import JSONEncoder
from flask import Flask, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///sakila.db"
db = SQLAlchemy(app)

class Bil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(80), unique=False, nullable=False)
    modell = db.Column(db.String(20), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)

db.create_all()

app.run()
