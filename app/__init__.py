from flask import Flask
app = Flask(__name__)
from app import routes

@app.route('/')
def index():
   return render_template('start.html')

if __name__ == '__main__':
   app.run(debug = True)