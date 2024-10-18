import cv2
import pytesseract
from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
import io
import os

# load model MobileNet-SSD
net = cv2.dnn.readNetFromCaffe('deploy.prototxt', 'mobilenet_iter_73000.caffemodel')

# Lista de clases que MobileNet-SSD puede detectar
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

# init Flask
app = Flask(__name__)

# post endpoint of images
@app.route('/process-image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file found'}), 400

    # read image from request
    file = request.files['image']
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))


    # change format image to be compatible with openCV
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # Get size of the image
    (h, w) = img.shape[:2]

    # process the image for the model (resize and normalize)
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    # list of detected objects
    detected_objects = []

    # process detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        # umbral of minimum confidence to consider a valid detection
        if confidence > 0.2:
            idx = int(detections[0, 0, i, 1])
            label = CLASSES[idx]
            detected_objects.append({
                'label': label,
                'confidence': float(confidence)
            })
            
    #TODO refactor get text from tesseract
    # # Get text from the image using Tesseract
    # gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # extracted_text = pytesseract.image_to_string(gray_image)

    # # Respuesta
    # response = {
    #     'extracted_text': extracted_text,
    #     'detected_objects': detected_objects
    # }
    
    response = {
        'detected_objects': detected_objects
    }
    return jsonify(response)

# Ruta para la verificación de estado
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Image API it''s running'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
