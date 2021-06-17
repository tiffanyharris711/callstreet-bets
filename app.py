from flask import Flask, render_template, request
<<<<<<< HEAD
import joblib
import numpy as np

app = Flask(__name__, template_folder='web')


@app.route('/')
def student():
    return render_template("home.html")
=======
from flask_bootstrap import Bootstrap
import joblib
import numpy as np

app = Flask(__name__, template_folder='templates')
Bootstrap(app)

@app.route('/')
def student():
    return render_template("index.html")
>>>>>>> d3c30e8160cd22bac2acf09fe9fe20ea42b05e35


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(-1, 1)
    loaded_model = joblib.load('model.sav')
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = round(float(ValuePredictor(to_predict_list)), 2)
<<<<<<< HEAD
        return render_template("home.html", result=result)
=======
        return render_template("index.html", result=result*100)
>>>>>>> d3c30e8160cd22bac2acf09fe9fe20ea42b05e35


if __name__ == '__main__':
    app.run(debug=True)