#!/usr/bin/python
import our_game

from flask import Flask, render_template, request, redirect, url_for
  
app = Flask(__name__)
@app.route('/')
def index():
   return render_template("start.html")


@app.route("/play")
def play():
    exec(open(our_game).read())

"""
@app.route('/text', methods=['GET', 'POST'])
def text(comments=[]):
    if request.method == "GET":
        return render_template("index.html", comments=comments)    
    comments.append(request.form["text_input"])  
    return redirect(url_for('text'))
"""
 
if __name__ == '__main__':
   app.run(debug=True)