from flask import Flask, render_template, request
import pickle
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

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
    model = load_model("algorithm/shapes_model.h5")
    # model_location = "algorithm/models/shapes_model-2.h5"

    return model.predict(img)
    # with open(model_location, "rb") as f:
    #     clf = pickle.load(f)
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
    result = None

    if prediction <= 0:
        result = f"The shape of the object is a Circle (Confidence: {(1 - prediction[0][0]): .1%})"
    else:
        result = f"The shape of the object is a Square (Confidence: {(prediction[0][0]): .1%})"

    return {"prediction": result}


if __name__ == '__main__':
    app.run(debug=True, port=5001)