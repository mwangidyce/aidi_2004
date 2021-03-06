from flask import Flask, render_template, request
import numpy as np
from PIL import Image
import pickle

app = Flask(__name__)


def load_image(image):
    #load the image

    # img = load_img(img, grayscale=False, target_size=(224, 224))
    #convert to array

    img = np.array(image)
    #reshape into a single sample with 1 channel
    img = img.reshape(1, 224, 224, 3)
    #prepare pixel data
    img = img.astype('float32')
    img = img / 255.0
    return img


def predict(image: str):
    img = load_image(image)
    with open("algorithm/models/model.pickle", "rb") as f:
        model = pickle.load(f)

    return model.predict(img)

    # return list(clf.predict(np.array(arr).reshape(1, -1)))[0]


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/upload/image", methods=["POST"])
def classify_api():
    img = None

    if request.files:
        for file in request.files.values():
            image = file
        # image loading and resizing
        img = Image.open(image)
        img = img.resize((224, 224))

    if img is None:
        return {"Prediction": "No Image Provided. Please re-upload."}

    prediction = predict(img)
    print(prediction[0][0])

    shape = "Circle" if prediction[0][0] <= 0.52 else "Square"

    result = None

    if prediction <= 0.5:
        result = f"The shape of the object is a {shape} (Confidence: {(1 - prediction[0][0]): .1%})"
    else:
        result = f"The shape of the object is a {shape} (Confidence: {(prediction[0][0]): .1%})"

    return {"prediction": result}


if __name__ == '__main__':
    app.run(debug=False)