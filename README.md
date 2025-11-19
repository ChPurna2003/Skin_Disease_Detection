🩺 Skin Disease Detection Web App

A lightweight Flask web application that predicts 8 types of skin diseases using image-based inference through a cloud API. Upload an image of a skin condition, and the model returns the predicted disease along with confidence scores.

---

🔍 Supported Skin Conditions

The model can identify the following diseases:

Acne

Eczema

Herpes Zoster (Shingles)

Hives

Lupus

Vitiligo

Raynaud’s Disease

Tinea (Ringworm)

---

🚀 Features

✔ Simple and clean web UI
✔ Image upload support
✔ Real-time prediction using cloud inference API
✔ JSON output for easy integration
✔ Lightweight Flask backend
✔ Fully deployable on Render / Railway / AWS

---

🛠️ Tech Stack

Frontend: HTML, CSS
Backend: Flask (Python)
Model Inference: Roboflow API
Other Libraries: OpenCV, Pillow, Requests
Hosting: Render (Gunicorn + Python)

---

📁 Project Structure
Skin_Disease_Detection/
│── templates/
│     ├── analyze.html
│     ├── app.html
│── static/
│── app.py
│── requirements.txt
│── Procfile
│── README.md

---

▶️ How It Works

User uploads a skin image via web interface

Backend sends the image to the cloud model

Model returns detected disease + confidence

Result is shown to the user as JSON or UI output

---

💡 Future Enhancements

Add disease descriptions + treatment suggestions

Multi-image batch support

History of previous detections

Improved UI/UX

Mobile optimized interface
