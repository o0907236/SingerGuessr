import urllib.request 
import json
from urllib.request import urlopen, Request
import flask
from flask import Flask, render_template, request
import json
import random
import pandas as pd
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  global title
  title = randomSong()
  return render_template('index.html',  title="Title: "+title)

@app.route('/answer', methods=['POST', 'GET'])
def game():
    if request.method == "POST":
      guess = request.form.get('guess')
      ans = answer(title)
      res = result(guess, title)
      if res:
        return render_template('index.html', title="Title: "+title, correct=True)
      
      else:
        return render_template('index.html', title="Title: "+title, incorrect=True, artist=ans)

def randomSong():
  titles = list(songs)
  rand_idx = random.randrange(len(titles))
  random_song = titles[rand_idx]
  return random_song

@app.route('/aboutus', methods=['GET'])
def aboutus():
    return render_template('aboutus.html')

file = open('songs.csv')
csvreader = csv.reader(file)


songs = {}
for row in csvreader:
  title = row[1]
  songs[title] = row[2]
  

def answer(title):
  return songs[title]

def result(guess, title):
  if songs[title].upper() == guess.upper():
    return True
  else:
    return False

if __name__ == "__main__":
 app.run(debug="True")
