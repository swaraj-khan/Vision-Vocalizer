import torch
from flask import Flask, render_template 
import cv2
import numpy as np
from flask_socketio import SocketIO, emit
import base64 

# Check for GPU availability
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load YOLOv7 model (make sure you have the correct model files in place)
model = torch.load('yolov5x6.pt')
print(model)
model_state_dict = model['model'].to(device)

app = Flask(__name__)
socketio = SocketIO(app)
def decode_image(data_image):
    try:
        # Split the base64 data into header and image data
        header, encoded = data_image.split(",", 1)  

        # Decode the base64 image data
        data = base64.decodebytes(encoded.encode('utf-8'))  

        # Load the image using OpenCV from the decoded data
        img = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)

        return img  
    except Exception as e:
        print(f"Error decoding image: {e}")
        return None  # Return None on error
    
@app.route('/')
def index():
    return render_template('index.html')  

@socketio.on('image')
def image(data_image):
    # Decode image data, process with YOLOv7, get results
    img = decode_image(data_image)  # You'll need a helper function for this 
    results = model(img) 
    boxes = results.xyxy[0].tolist()
    class_names = results.pandas().xyxy[0]['name'].tolist()

    # Emit results back to the frontend
    emit('response_back', {'boxes': boxes, 'classes': class_names})

if __name__ == '__main__':
    socketio.run(app, debug=True)
