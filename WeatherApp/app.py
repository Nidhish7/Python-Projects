from flask import Flask, render_template, request
from weatherApp import getWeather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            weather = getWeather(city.strip())
            if weather:
                return render_template("result.html", weather=weather)
            else:
                error = "City not found, please try again."
                return render_template("index.html", error=error)
        else:
            error = "Please enter a city name."
            return render_template("index.html", error=error)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
