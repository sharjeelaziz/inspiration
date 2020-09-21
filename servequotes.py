import webbrowser
import json
from flask import Flask, render_template, abort
import requests
import random
from nocache import nocache

app = Flask(__name__)

@app.route("/")
@nocache
def wisdom():
    quoteList = get_random_quote()
    if not quoteList:
        error = 'Error loading quotes'
        return render_template('index.html', error=error), 500
    
    random_number = random.randint(1, 1000)

    return render_template('index.html', quote=quoteList[0][0], author=quoteList[0][1],
        quote1=quoteList[1][0], author1=quoteList[1][1],
        quote2=quoteList[2][0], author2=quoteList[2][1],
        quote3=quoteList[3][0], author3=quoteList[3][1],
        quote4=quoteList[4][0], author4=quoteList[4][1],
        quote5=quoteList[5][0], author5=quoteList[5][1],
        random_number=random_number)


def get_random_quote():
    f = open('quotes.json', )
    data = json.load(f)
    quoteList = []

    try:
        for x in range(6):
            y = random.choice(data['quotes'])
            quoteList.append((y['text'], y['author']))
    except IndexError:
        print("nothing found")

    f.close()
    return quoteList

if __name__ == "__main__":
    app.run(host='0.0.0.0')

