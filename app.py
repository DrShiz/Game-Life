from pickle import TRUE
from flask import Flask, render_template
from game_of_life import GameOfLife


app = Flask(__name__)

@app.route('/')
def main():
    GameOfLife(25, 25)
    return render_template('index.html')

@app.route('/life')
def life():
    gom = GameOfLife()
    if gom.counter > 0:
        gom.form_new_generation()
    gom.counter += 1
    return render_template('life.html', gom=gom)

if __name__ == '__main__':
    app.run(debug=True)

