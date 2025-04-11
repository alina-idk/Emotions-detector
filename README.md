# Emotions-detector
# 🎭 Live Emotion Detector

This project is a web application that detects a person's emotions in real time using their webcam. It uses **DeepFace** for facial emotion analysis and **FastAPI** as the backend framework.

## 🚀 Features

- Automatically detects facial emotions in real time
- Uses webcam video input
- Clean and intuitive interface with TailwindCSS
- Fast and modern backend powered by FastAPI

## 🧰 Technologies Used

- FastAPI
- DeepFace
- TensorFlow
- OpenCV
- NumPy
- Pillow
- TailwindCSS (for frontend styling)

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alina-idk/Emotions-detector.git
   cd emotion-detector

   
2. (Optional but recommended) Create a virtual environment:

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate


3. Install Python dependencies
pip install -r requirements.txt


4. Run the FastAPI backend
uvicorn main:app --reload

5. Open the frontend Open index.html in your browser. It will start your webcam and send frames to the backend for emotion detection every 2 seconds.


⚠️ Notes
On the first run, DeepFace will automatically download the required pre-trained models.

You must allow camera access in your browser for real-time detection to work.

Make sure the backend is running at http://localhost:8000 or update the fetch URL in your index.html.



 ❤️ Built with Love
Made using Python, FastAPI, and a touch of joy 😊
Feel free to improve, fork, or share!

