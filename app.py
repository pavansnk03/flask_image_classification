from flask import Flask, request, render_template, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r'/home/Hadoop/Desktop/pnsnk/SE/04_flask_ML/static/uploads'

model = load_model(r'/home/Hadoop/Desktop/pnsnk/SE/04_flask_ML/cifar10_model.h5')
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

def predict_image(file_path):
    img = load_img(file_path, target_size=(32, 32))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    return class_names[predicted_class]

@app.route('/')
def index():
    image_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', image_files=image_files)

@app.route('/classify/<filename>')
def classify_image(filename):
    # Get the file path of the image
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Make a prediction
    prediction = predict_image(file_path)

    return render_template('result.html', filename=filename, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
