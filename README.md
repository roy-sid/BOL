# BOL
for Triwizard hackathon

What is bol?
bol is a real-time object recognition and translation app that uses your camera to identify objects, translate their names into another language, and provide rich cultural context — like where the object is used, in which festivals, folk stories, and more.

Whether you’re learning Hindi, Bengali, or Tamil — bol lets you experience a language through your eyes, not just words.

Features
📸 Real-time camera object detection (YOLO/MobileNet)
🌐 Live translation of detected object labels
🧧 Cultural info (festivals, stories, regional significance)
📱 Clean and responsive UI
🔐 Modular backend with FastAPI
🌈 Language support extensible with minimal config

Tech Stack
Frontend:
React, TailwindCSS, Axios, React Webcam, React Router

Backend:
FastAPI, Uvicorn, Python, YOLOv5/MobileNet, OpenCV, MongoDB

Folder Structure
bol/
├── bol_frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.js
│   └── package.json
├── bol_backend/
│   ├── main.py
│   ├── detect.py
│   ├── translate.py
│   ├── culture.py
│   └── requirements.txt
└── README.md

Getting Started

1. Clone the repo
git clone https://github.com/your-username/bol.git
cd bol

2. Frontend Setup (React)
cd frontend
npm install
npm run start

3. Backend Setup (FastAPI)
cd backend
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload


How It Works
1. Open the camera via the UI
2. The backend detects the object using a lightweight model (YOLO/MobileNet)
3. Translates the object name into the chosen language
4. Fetches cultural information from MongoDB (festivals, stories, etc.)
5. Displays it all on-screen — in real-time!

Innovation Highlights
1. Combines Computer Vision + Language Learning + Culture
2. Real-time interaction through object detection
3. Cultural immersion through festivals, rituals, and stories
4. Easy to scale to other Indian and global languages

Contributors
Ankita Jha – Frontend, ML Integration, Cultural content
Siddhant Roy – Backend, FastAPI, YOLO/MobileNet integration
