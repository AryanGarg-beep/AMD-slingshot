# AI Smart Glasses – Object Detection Prototype

## Overview

This project is an early-stage prototype of an assistive smart glasses system designed for visually impaired users.

The system captures visual input using a camera and performs real-time object detection using YOLOv8. The detected objects are then intended to be converted into auditory feedback (future implementation).

This repository currently contains a minimal, barebones YOLOv8-based object detection pipeline written in Python.

---

## Objective

To detect objects in real-time from a video stream and lay the foundation for:

- Obstacle awareness
- Directional feedback (e.g., "Door slightly left")
- Scene understanding
- Assistive auditory guidance

Future upgrades will replace YOLOv8 with InstaLLA-VL for advanced multimodal understanding.

---

## Current Implementation

- YOLOv8 for object detection
- Real-time webcam inference
- Bounding box visualization
- Confidence score display

This version does NOT yet include:
- Audio output
- Bluetooth communication
- Mobile app integration
- Depth estimation
- Context-aware scene description

---

## Planned Upgrade: InstaLLA-VL

The next phase will integrate InstaLLA-VL (Vision-Language Model) to enable:

- Context-aware scene descriptions
- Natural language feedback
- Better spatial awareness reasoning
- Multimodal understanding

This will significantly improve assistive capabilities compared to standard object detection.

---

## Installation

### 1.Clone Repository

```bash
git clone https://github.com/AryanGarg-beep/AMD-slingshot.git
cd AMD-slingshot
 ```

### 2. Create a VM
```bash
#On MacOS/Linux
python3 -m venv venv
source venv/bin/activate


#windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install ultralytics
```

### 4. Run the program
```bash
#In the AMD-slingshot folder
python app.py
```
## To run the ESP-32 camera
```bash
#copy you url and paste in "server-url" in the .ino file
ip a #Get IP from this

#Make sure server is active before running the ESP, If HTTP-error comes up, check if the IP matches
python server.py
```
