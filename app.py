from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import numpy
import pandas as pd
import scrape_energy


# Create flask routes
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/energy_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    energy_data = mongo.db.energy.find_one()

    return render_template("index.html", energy_data=energy_data)


@app.route("/scrape")
def dataframe():
    energy = mongo.db.energy

    energy_data = scrape_energy.scrape()
    
    energy.update({}, energy_data, upsert=True)
    
    return redirect("/", code=302)

@app.route("/data")
def data():
    energy_data = mongo.db.energy.find_one()

    energy_data.pop('_id')
    
    top_df = pd.DataFrame(energy_data)
    
    big_spenders = []    
    for i in range(len(top_df)):
        if top_df.population[i] != 0 and top_df.gdppc[i] != 0:
            calculation = (top_df.econsumption[i] / top_df.population[i]) / top_df.gdppc[i]
            big_spenders.append(calculation)
        elif top_df.population[i] == 0 or top_df.gdppc[i] == 0:
            big_spenders.append(0)

    top_df["big_spenders"] = big_spenders

    top_df.sort_values(by=["big_spenders"], ascending=False, inplace=True)
    top_population = top_df.to_dict("list")

    return jsonify(top_population)

if __name__ == "__main__":
    app.run()

# Step 1: alter app.js
# Step 2: run "mongod" in terminal
# Step 3: run "python app.py" in ANOTHER terminal
# Step 4: go to "localhost:5000/scrape" in browser
