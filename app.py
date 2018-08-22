from flask import Flask, render_template
import pandas as pd
import random

app = Flask(__name__)
app.debug = True


def get_word(definition=True):
    df = pd.read_csv('words.csv')

    # 단어 랜덤 선택
    word = random.choice(df['word'])
    meaning = df[df['word'] == word]['meaning'].values[0]

    # 다른 보기 만들기
    other = random.sample(set(df[df['meaning'] != meaning]['meaning']), 3)
    other.append(meaning)
    if definition:
        return word, meaning
    else:
        return word, other


@app.route('/')
def home():
    word, other = get_word(definition=False)
    print(other)
    return render_template('home.html', word=word, other=other)


@app.route('/study')
def study():
    word, meaning = get_word(True)
    return render_template('study.html', word=word, meaning=meaning)


if __name__ == '__main__':
    app.run()
