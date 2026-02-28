from flask import Flask, request, jsonify
import numpy as np
import cv2
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO("yolov8n.pt")  # lightweight model


@app.route("/detect", methods=["POST"])
def detect():
    file_bytes = request.data
    np_arr = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    results = model(img, conf=0.2, verbose=False)

    if len(results[0].boxes) > 0:
        cls = int(results[0].boxes.cls[0])
        conf = float(results[0].boxes.conf[0])
        label = model.names[cls]
        return jsonify({"label": f"{label} {conf:.2f}"})
    else:
        return jsonify({"label": "Nothing"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
