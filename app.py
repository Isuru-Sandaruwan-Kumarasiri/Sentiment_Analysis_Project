from flask import Flask, render_template,request,redirect,jsonify
from helper import preprocessing,vectorizar,get_prediction

app = Flask(__name__)

reviews = ["Good Product", "Bad Product", "I like it"]
positive = 0
negative = 0

@app.route('/')
def index():
    data = dict()
    data["reviews"] = reviews
    data["positive"] = positive
    data["negative"] = negative
    return render_template('index.html', data=data)


@app.route("/",methods=['post'])
def my_post():
    text = request.form['text']
    pre_text=preprocessing(text)
    vect_text=vectorizar(pre_text)
    pred=get_prediction(vect_text)

    print(pred)

    if pred =='negative':
        global negative
        negative+=1
    else:
        global positive
        positive+=1

    reviews.insert(0,text)
    return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)
