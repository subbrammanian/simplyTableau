from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Ricardo'}  # fake user
	return render_template('index.html',title="MainPage",user=user)