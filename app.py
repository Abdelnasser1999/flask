import os
import pickle
import sklearn
import numpy as np
import keras
from flask import Flask, request, jsonify, render_template, redirect
model, training_accuracy, testing_accuracy = pickle.load(open("SVM.pkl","rb"))

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "C:/Users/HP/PycharmProjects/pythonProject"


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            print(image)
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            return jsonify({
                'type = ': 'Model2',
                'image name =': str(image.filename)
            })
    return render_template("upload_image.html")


@app.route('/model1', methods=["GET", "POST"])
def hello2():
    record = request.args['record']
    arr1=record.split(",")
    arr2=[]
    for a in arr1:
        arr2.append(int(a))
    result = model.predict(np.array([arr2]))
    return jsonify({
        'type = ': 'Model1',
        'result =': str(result),
        'training_acc': str(training_accuracy),
        'testing_acc': str(testing_accuracy)
    })


@app.route('/')
def index():
    return jsonify({'Service': 'Flask',
                    'massage': 'Flask says Hello From AWS'})


if __name__ == '__main__':
    app.run(debug=True)
