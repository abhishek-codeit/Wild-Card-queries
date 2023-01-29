# write a flask app that can run a html file
# and can also run a python file

from flask import Flask, render_template, request
from algorithm import *
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    # how to run a function from algorithm.py
    # and pass the query to it
    # and return the result
    # and display it in the html file
    answer = Wsearch(query)
    return render_template('output.html',tables=[answer.to_html(classes='data')], titles=answer.columns.values)
    
    
    
    # return 'Code executed'
    
if __name__ == '__main__':
    app.run()



# Run the app.py file


