import os
from flask import Flask, render_template, session, redirect, url_for
from flask_script import Shell
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

# Configure base directory of app
basedir = os.path.abspath(os.path.dirname(__file__))

# Application configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardtoguessstringfromsi364thisisnotsupersecurebutitsok'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # For database use

#########
######### Everything above this line is important setup, not problem-solving.
#########

##### Set up Models #####
## Task 1: Write models for the tables Actor and Director

class Movie(db.Model):
    __tablename__ = 'movies'
    movieId = db.Column(db.Integer, primary_key=True)
    movieTitle = db.Column(db.String(64))
    movieGenre = db.Column(db.String(32))

    def __repr__(self):
        return '<Movie %r>' % self.movieTitle

class Actor(db.Model):
    pass

class Director(db.Model):
    pass


##### Getting data from tables #####

## TASK 2 : Write a route that gets all the actors. You may create different template to render the results.
@app.route('/list-of-movies')
def listOfMovies():
    allMovies = Movie.query.all()
    return render_template('list_of_movies.html', results = allMovies)

## TASK 3 :
### 1. Write a route that gets all sci-fi movies.
### 2. Write a route that gets all the actors who have starred in “Star Wars: The Force Awakens”


##### Adding data to tables #####
## TASK 4 & 5
@app.route('/enter-director')
def addDirector():
    return render_template('director-form.html')

@app.route('/director-added', methods = ['GET','POST'])
def addDirector():
    # Add the details of the director to the director table
    pass


## BONUS CHALLENGE
@app.route('/enter-moviename')
def addMovie():
    return render_remplate('movie-form.html')

@app.route('/movie-added', methods = ['GET','POST'])
def addMovie():
    # Get data using OMDB API and add it to the relevant tables
    pass

if __name__=='__main__':
    manager.run()
