from flask import Flask, render_template

app = Flask(__name__)

reviews = ["Good Product", "Bad Product", "I like it"]
positive = 7
negative = 8

@app.route('/')
def index():
    data = dict()
    data["reviews"] = reviews
    data["positive"] = positive
    data["negative"] = negative
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
