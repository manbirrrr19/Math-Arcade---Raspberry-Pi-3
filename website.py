from flask import Flask, render_template, request
import datetime
import json
import time
import main_mathgame

app = Flask(__name__)

gamedata_file = 'gamedata.json'

def load_game_data():
    try:
        with open(gamedata_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save sales data to file
def save_game_data(game_data):
    with open(gamedata_file, 'w') as f:
        json.dump(game_data, f)

def update_game_data(regnum, points, game_mode):
    game_data = load_game_data()
    timestamp = datetime.datetime.now()
    game = {'regnum': str(regnum), 'timestamp': str(timestamp), 'difficulty': game_mode, 'score': points}
    game_data.append(game)
    save_game_data(game_data)

@app.route('/')
def home():
    game_data = load_game_data()
    return render_template("home.html", game_data=game_data)

def website_run():
    app.run(debug=True,host='0.0.0.0', port=5001, use_reloader=False)
    time.sleep(10)

if __name__ == "__main__":
    website_run()