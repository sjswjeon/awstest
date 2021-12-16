from sqlalchemy.exc import SQLAlchemyError
from pyweb import app
from flask import render_template, request, Response
from pyweb.init_db import db_session
from pyweb.models import Message

@app.route("/")
def idx():
    messages = Message.query.all()
    return render_template('index.html', messages = messages)

@app.route("/", methods=['POST'])
def save():
    content = request.form.get('content')
    m = Message(content)
    db_session.add(m)
    db_session.commit()

    messages = Message.query.all()

    return render_template('index.html', messages = messages)