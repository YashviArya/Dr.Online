from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
@app.route("/dashboard")
@app.route("/")
def hello_world():
    return render_template('patientdashboard.html')


@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/login")
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
