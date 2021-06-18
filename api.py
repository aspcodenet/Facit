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

    def serialize(self):
        return {
            'modell': self.modell,
            'namn': self.namn,
            'year': self.year,
            'id': self.id
        }    



@app.route('/api/bil', methods=['GET'])
def listaAlla():
    q = Bil.query.all()
    return jsonify([b.serialize() for b in q])



# REST API
# /api/bil = GET  LISTA PÅ ALLA
# /api/bil/1 = GET  SE EN BIL
# /api/bil = POST  json som ny NY
# /api/bil/1 = DELETE  delete
# /api/bil/1 = PUT/PATCH  udate

# b = Bil()
# b.namn = "Volvo"
# b.modell = "XC60"
# b.year = 2016

# b2 = Bil()
# b2.namn = "Saab"
# b2.modell = "V4"
# b2.year = 1973


# db.session.add(b)                       
# db.session.add(b2)                       
# db.session.commit()


#db.create_all()

app.run()
