from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def hello():
    name="Ashar"
    return render_template('index.html',name2=name)

app.run(debug=True)

    