########################################################################################
######################          Import packages      ###################################
########################################################################################
from flask import Blueprint, render_template, flash, request
from flask_login import login_required, current_user
from __init__ import create_app, db
from os import *
from datetime import date

########################################################################################
# our main blueprint
main = Blueprint('main', __name__, static_folder = 'static', template_folder = 'templates')
start_day = date(2022, 4, 12)

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')

@main.route('/profile') # profile page that return 'profile'
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/edit', methods=['POST', 'GET']) # edit today's file
@login_required
def edit():
	id = current_user.id
	cur_day = (date.today()-start_day).days
	text = ""
	if request.method == 'POST':
		print(request)
	if path.exists(f'./{id}/{id}_{cur_day}.md'):
		text = openfile(f'./{id}/{id}_{cur_day}.md', "r").readlines()
	return render_template("editor.html", text=text)

@main.route('/read') # read today's recap
@login_required
def read():
	text = ""
	id = current_user.id
	day = (date.today()-start_day).days-1
	fn = 1
	fnn = 1
	while day >= 0:
		if path.exists(f'./{id}/{id}_{day}.md'):
			text += "Day " + str(day)+"\n\n"+openfile(f'./{id}/{id}_{day}.md', "r").readlines() + "\n\n"
		day -= fnn
		fnn += fn
		fn = fnn
	return render_template("editor.html", text=text)

app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode
