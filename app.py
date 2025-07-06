from flask import Flask, render_template,request,redirect,jsonify
from helper import preprocessing,vectorizar,get_prediction
from logger import logging

app = Flask(__name__)
logging.info("Flask server started")
reviews = []
positive = 0
negative = 0

@app.route('/')
def index():
    data = dict()
    data["reviews"] = reviews
    data["positive"] = positive
    data["negative"] = negative
    logging.info('========== Open home page ============')
    return render_template('index.html', data=data)


@app.route("/",methods=['post'])
def my_post():
    text = request.form['text']
    logging.info(f'Text : {text}')
    pre_text=preprocessing(text)
    logging.info(f'Preprocessed Text : {pre_text}')
    vect_text=vectorizar(pre_text)
    logging.info(f'Vectorized Text : {vect_text}')
    pred=get_prediction(vect_text)
    logging.info(f'Prediction : {pred}')



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
