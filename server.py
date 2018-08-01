from flask import Flask, render_template

app = Flask(__name__)

@app.route("/ninjas")
def ninjas():

    @app.route("/ninjas/<color>") # for some reason wouldn't launch the site unless this was indented??????????
    def turtle(color):
        turtle == ""
        if color == "blue":
            turtle = "blue.jpg"
        elif color == "orange":
            turtle = "orange.jpg"
        elif color == "red":
            turtle = "red.jpg"
        elif color == "purple":
            turtle = "purple.jpg"
        else:
            turtle = "notapril.jpg"

    session["color"] = turtle   
    return  render_template("ninja.html")


app.run(debug=True)