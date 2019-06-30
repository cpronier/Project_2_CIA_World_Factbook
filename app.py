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
def scrape():
    energy = mongo.db.energy

    energy_data = scrape_energy.scrape()
    
    energy.update({}, energy_data, upsert=True)
    
    return redirect("/", code=302)

@app.route("/data1")
def data1():
    energy_data = mongo.db.energy.find_one()

    energy_data.pop('_id')
    
    top_consumers1_df = pd.DataFrame(energy_data)
    
    top_consumers1_df.sort_values(by=["econsumptionpc"], ascending=False, inplace=True)
    
    top_consumers1 = top_consumers1_df.to_dict("list")

    return jsonify(top_consumers1)

@app.route("/data1_without_IS_MH")
def data1_without_IS_MH():
    energy_data = mongo.db.energy.find_one()

    energy_data.pop('_id')
    
    top_consumers2_df = pd.DataFrame(energy_data)
    
    top_consumers2_df.sort_values(by=["econsumptionpc"], ascending=False, inplace=True)
    top_consumers2_df = top_consumers2_df[top_consumers2_df.name != 'Marshall Islands']
    top_consumers2_df = top_consumers2_df[top_consumers2_df.name != 'Iceland']
    
    top_consumers2 = top_consumers2_df.to_dict("list")

    return jsonify(top_consumers2)

@app.route("/econsumption")
def econsumption():

    return render_template("econsumption.html")

@app.route("/econsumption_wo")
def econsumption_wo():

    return render_template("econsumption_wo.html")


@app.route("/data2")
def data2():
    energy_data = mongo.db.energy.find_one()

    energy_data.pop('_id')
    
    top_spenders1_df = pd.DataFrame(energy_data)
    
    top_spenders1_df.sort_values(by=["little_big_spenders"], ascending=False, inplace=True)
    
    top_spenders1 = top_spenders1_df.to_dict("list")

    return jsonify(top_spenders1)

@app.route("/data2_without_IS_MH")
def data2_without_IS_MH():
    energy_data = mongo.db.energy.find_one()

    energy_data.pop('_id')
    
    top_spender2_df = pd.DataFrame(energy_data)
    
    top_spender2_df.sort_values(by=["little_big_spenders"], ascending=False, inplace=True)
    top_spender2_df = top_spender2_df[top_spender2_df.name != 'Marshall Islands']
    top_spender2_df = top_spender2_df[top_spender2_df.name != 'Iceland']
    
    top_spender2 = top_spender2_df.to_dict("list")

    return jsonify(top_spender2)


@app.route("/little_big_spenders")
def little_big_spenders():

    return render_template("little_big_spenders.html")

@app.route("/little_big_spenders_wo")
def little_big_spenders_wo():

    return render_template("little_big_spenders_wo.html")


if __name__ == "__main__":
    app.run()

# Step 1: alter app.js
# Step 2: run "mongod" in terminal
# Step 3: run "python app.py" in ANOTHER terminal
# Step 4: go to "localhost:5000/scrape" in browser
