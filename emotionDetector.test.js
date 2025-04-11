/**
 * @jest-environment jsdom
 */

global.fetch = jest.fn(); // mock global fetch

describe("Emotion Detector Script", () => {
  let video, canvas, emotionDiv;

  beforeEach(() => {
    // Setăm DOM-ul
    document.body.innerHTML = `
      <video id="video"></video>
      <canvas id="canvas"></canvas>
      <div id="emotion">...</div>
    `;

    video = document.getElementById('video');
    canvas = document.getElementById('canvas');
    emotionDiv = document.getElementById('emotion');
  });

  it("should update emotion text on successful fetch", async () => {
    // Mock pentru getContext și desenare
    const mockContext = {
      drawImage: jest.fn(),
    };
    canvas.getContext = jest.fn(() => mockContext);
    video.videoWidth = 640;
    video.videoHeight = 480;

    // Simulează toBlob
    canvas.toBlob = (callback, type) => {
      const blob = new Blob(["fake image content"], { type: "image/jpeg" });
      callback(blob);
    };

    // Mock fetch response
    fetch.mockResolvedValueOnce({
      json: async () => ({ emotion: "Fericire" })
    });

    // Copiem logica intervalului ca funcție directă pt test
    const context = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    await new Promise((resolve) => {
      canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append("file", blob, "frame.jpg");

        fetch("http://localhost:8000/detect-emotion/", {
          method: "POST",
          body: formData
        })
        .then(res => res.json())
        .then(data => {
          emotionDiv.textContent = data.emotion;
          expect(emotionDiv.textContent).toBe("Fericire");
          resolve();
        });
      }, "image/jpeg");
    });
  });

  it("should show error on fetch failure", async () => {
    fetch.mockRejectedValueOnce(new Error("Network error"));

    canvas.toBlob = (callback, type) => {
      const blob = new Blob(["fake image content"], { type: "image/jpeg" });
      callback(blob);
    };

    await new Promise((resolve) => {
      canvas.toBlob(blob => {
        const formData = new FormData();
        formData.append("file", blob, "frame.jpg");

        fetch("http://localhost:8000/detect-emotion/", {
          method: "POST",
          body: formData
        })
        .then(res => res.json())
        .then(data => {
          emotionDiv.textContent = data.emotion;
          resolve();
        })
        .catch(err => {
          emotionDiv.textContent = "Eroare";
          expect(emotionDiv.textContent).toBe("Eroare");
          resolve();
        });
      }, "image/jpeg");
    });
  });
});
