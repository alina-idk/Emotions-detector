import pytest
from fastapi.testclient import TestClient
from PIL import Image
import io
import numpy as np

from main import app  # presupun că fișierul tău se numește main.py

client = TestClient(app)

# Creează o imagine dummy pentru test
def create_dummy_image():
    image = Image.new("RGB", (100, 100), color="red")
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format="JPEG")
    img_byte_arr.seek(0)
    return img_byte_arr

def test_detect_emotion_success(mocker):
    dummy_image = create_dummy_image()

    # Mock pentru DeepFace.analyze
    mocker.patch("main.DeepFace.analyze", return_value=[{"dominant_emotion": "happy"}])

    response = client.post(
        "/detect-emotion/",
        files={"file": ("dummy.jpg", dummy_image, "image/jpeg")}
    )

    assert response.status_code == 200
    assert response.json() == {"emotion": "happy"}

def test_detect_emotion_failure(mocker):
    dummy_image = create_dummy_image()

    # Forțăm o excepție în DeepFace.analyze
    mocker.patch("main.DeepFace.analyze", side_effect=Exception("Test error"))

    response = client.post(
        "/detect-emotion/",
        files={"file": ("dummy.jpg", dummy_image, "image/jpeg")}
    )

    assert response.status_code == 500
    assert response.json() == {"message": "Eroare la procesarea imaginii."}
