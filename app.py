from flask import Flask, render_template
from bulbs import solve_minimum_bulbs

app = Flask(__name__)

@app.route('/')
def home():
    room, n_room = solve_minimum_bulbs()

    return render_template('index.html', n=n_room, room=room)

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)

