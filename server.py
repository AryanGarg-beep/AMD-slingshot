from flask import Flask, request, jsonify
import numpy as np
import cv2
from ultralytics import YOLO
import threading

app = Flask(__name__)
model = YOLO("yolov8n.pt")

latest_frame = None


@app.route("/detect", methods=["POST"])
def detect():
    global latest_frame

    try:
        file_bytes = request.data
        np_arr = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if img is None:
            return jsonify({"label": "Invalid Image"})

        results = model(img, conf=0.2, verbose=False)

        annotated = results[0].plot()
        latest_frame = annotated

        if len(results[0].boxes) > 0:
            cls = int(results[0].boxes.cls[0])
            conf = float(results[0].boxes.conf[0])
            label = model.names[cls]
            return jsonify({"label": f"{label} {conf:.2f}"})
        else:
            return jsonify({"label": "Nothing"})

    except Exception as e:
        print("Error:", e)
        return jsonify({"label": "Server Error"})


def show_window():
    global latest_frame
    while True:
        if latest_frame is not None:
            cv2.imshow("ESP32 YOLO Feed", latest_frame)
            cv2.waitKey(1)


if __name__ == "__main__":
    threading.Thread(target=show_window, daemon=True).start()
    app.run(host="0.0.0.0", port=5000, threaded=True)
