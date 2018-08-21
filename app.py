from flask import Flask, render_template
import pandas as pd
import random

app = Flask(__name__)
app.debug = True


@app.route('/')
def home():
    return render_template('home.html')


# @app.route('/about')
# def hello_world():
#     df = pd.read_csv('words.csv')
#     word = random.choice(df['word'])
#     return word


if __name__ == '__main__':
    app.run()
