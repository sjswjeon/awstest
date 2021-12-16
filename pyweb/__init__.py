from flask import Flask, render_template
from pyweb.init_db import init_database, db_session

app = Flask(__name__)
import pyweb.views

app.debug = True
