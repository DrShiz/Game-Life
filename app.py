from crypt import methods
from pickle import TRUE
from flask import Flask, render_template
from game_of_life import GameOfLife
from flask import request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        width = request.form.get['width']
        height = request.form.get('height')
    else:
        width = 15
        height = 15
    GameOfLife(width, height)
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

