from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from deepface import DeepFace
import shutil
import uuid
import os
import io
from PIL import Image
import numpy as np

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

app = FastAPI()

# Permite accesul frontend-ului (dacă rulează pe alt port)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # poți pune "http://localhost:3000" sau alt domeniu
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/detect-emotion/")
async def detect_emotion(file: UploadFile = File(...)):
    try:
        # Citește fișierul ca imagine
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))

        # Convertește imaginea în numpy array
        img_array = np.array(image)

        # Folosește DeepFace pentru a detecta emoțiile
        result = DeepFace.analyze(img_path=img_array, actions=['emotion'])

        # Returnează rezultatul (emoțiile detectate)
        return JSONResponse(content={"emotion": result[0]['dominant_emotion']})

    except Exception as e:
        print(f"Eroare la procesarea imaginii: {e}")
        return JSONResponse(status_code=500, content={"message": "Eroare la procesarea imaginii."})