#  Skin Disease Detection App

This is a simple web application that detects skin diseases from uploaded images using a computer vision model.

I built this project to learn how to take an AI model and actually deploy it like a real-world application using AWS and DevOps tools.

---

## Live Demo

👉 http://13.232.191.7:5000

---

##  Tech Stack

- Python
- Flask
- Docker
- AWS EC2
- GitHub Actions (CI/CD)
- Roboflow API (for model predictions)

---

##  How It Works

1. User uploads an image through the web interface  
2. Flask backend receives the image  
3. Image is sent to Roboflow API  
4. Model returns prediction  
5. Result is shown to the user  

---

## 🐳 Docker Setup

Build the image:

```bash
docker build -t skin-app .


Run the container: docker run -d -p 5000:5000 skin-app
