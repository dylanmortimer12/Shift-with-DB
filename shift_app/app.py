from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
db.create_all()

from models import *

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/addPlay", methods = ['POST'])
def addPlay():
    name = request.values.get('name', '')
    cy = request.values.get('cy', '')
    cx = request.values.get('cx', '')
    hit_angle = request.values.get('hit_angle', '')
    balls = request.values.get('balls', '')
    strikes = request.values.get('strikes', '')
    phand = request.values.get('pitcher', '')
    bhand = request.values.get('hitter', '')

    print("INSERT INTO PLAY_BY_PLAY (BATTER_NAME,PITCHER_HAND,BATTER_HAND,STRIKES,BALLS,CX,CY,HIT_DIRECTION) VALUES ('" + str(name) + "' ,'" + phand + "','" + bhand + "'," + strikes +"," + balls + "," + cx +"," + cy + "," + hit_angle + ");")

    # db.engine.execute("INSERT INTO PLAY_BY_PLAY (BATTER_NAME,PITCHER_HAND,BATTER_HAND,STRIKES,BALLS,CX,CY,HIT_DIRECTION) VALUES ('" + str(name) + "' ,'" + phand + "','" + bhand + "'," + strikes +"," + balls + "," + cx +"," + cy + "," + hit_angle + ");")

    new_row = play_by_play(name,phand,bhand,strikes,balls,cx,cy,hit_angle)
    try:
        db.session.add(new_row)
    except:
		return {'result': 'upload failed'}
    
    db.session.commit()
    # print(db.engine.execute('SELECT * FROM PLAY_BY_PLAY;'))
    return 'done'

