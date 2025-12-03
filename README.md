markdown
Hand Gesture Recognition (Python, OpenCV, CVZone)

This project is a simple real-time hand gesture recognition system built with  
Python, OpenCV (cv2), and CVZone.

Depending on the detected gesture, the program displays one of three images:

- ✌️ Victory / V sign
- 🖕 Middle finger
- ✋ High-five / Open hand

---

 🚀 Features
- Real-time webcam hand tracking  
- Gesture detection using CVZone's `HandDetector`
- Automatically displays different images based on the gesture
- Works inside a virtual environment (Python 3.12+)

---

 🛠️ Tech Stack
- Python 3.12
- OpenCV (cv2)
- CVZone
- Mediapipe (indirectly used inside CVZone)

---

 📁 Project Structure


HandGesture/
│
├── HandGesture.py           Main script (gesture detection + display)
├── Bears/
│   ├── v_image.jpeg         V sign image
│   ├── middle_image.jpg     Middle finger image
│   ├── highfive_image.jpg   High-five image
│
├── .gitignore
└── requirements.txt


---

 ▶️ How to Run

 1) Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
````

 2) Install dependencies

```bash
pip install opencv-python cvzone
```

 3) Run the program

```bash
python HandGesture.py
```

---

 ✋ Supported Gestures

Victory / V ✌️   - Index + middle finger up - Shows v_image.jpeg
Middle finger 🖕 - Middle finger only       - Shows middle_image.jpg
High-five ✋     - All fingers extended     - Shows highfive_image.jpg

---

 📝 Future Improvements

 Add more gestures (OK sign, fist, thumbs up)
 Add sound or animation per gesture
 Improve detection accuracy with custom ML model
 Add UI buttons and WebSocket streaming

---

 📄 License

MIT License
Feel free to use or modify the code.

---

 🙌 Author

Developed by Jinwoong
GitHub: [Real-Woong](https://github.com/Real-Woong)

