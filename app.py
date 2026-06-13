from flask import Flask, request, render_template
import joblib
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model = joblib.load('savedmodel.pth')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('index.html', prediction="No file uploaded")
    
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', prediction="No file selected")

    # Read and preprocess image
    img = Image.open(io.BytesIO(file.read())).convert('L')
    img = img.resize((64, 64))
    img_array = np.array(img).flatten().reshape(1, -1) / 255.0

    prediction = model.predict(img_array)
    return render_template('index.html', prediction=f"Predicted Person ID: {prediction[0]}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
