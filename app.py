from flask import Flask, render_template
from game_of_life import GameOfLife
from flask import request, jsonify


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        width = int(request.form['width'])
        height = int(request.form['height'])
        GameOfLife(width, height)
        return {}
    else:
        return render_template('index.html')

@app.route('/life', methods=['GET', 'POST'])
def life():
    gol = GameOfLife()
    if gol.counter > 0:
        gol.form_new_generation()
    if request.method == 'POST':
        gol.counter += 1
        return jsonify(world=gol.world, counter = gol.counter, old_world=gol.old_world)
    else:
        return render_template('life.html', counter = gol.counter)

if __name__ == '__main__':
    app.run(debug=True)

