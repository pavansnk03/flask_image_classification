# Image Classifier Web App

## Overview
This project is a web-based image classifier built using **Flask** and **TensorFlow**. It allows users to upload images from a gallery, which are then classified using a pre-trained **CIFAR-10 model**. The result is displayed directly on the webpage.

## Features
✅ Uploads and classifies images from a gallery
✅ Uses a **CIFAR-10** pre-trained model for image recognition
✅ Displays predictions clearly with an intuitive UI
✅ Stylish design with **smooth animations** and **responsive layout**

## Technologies Used
- **Python** (For the backend logic)
- **Flask** (For the web framework)
- **TensorFlow** (For model prediction)
- **Pillow** (For image preprocessing)
- **HTML, CSS** (For frontend design and animations)

## Prerequisites
Ensure you have the following installed:
- Python 3.8 or above
- Pip (Python package installer)

## Installation
1. **Clone the Repository**

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Add Images for Testing**
Place your test images inside the `static/uploads` folder.

4. **Run the Application**
```bash
python app.py
```

5. **Access the Web App**
Go to [http://localhost:5000](http://localhost:5000) in your browser.

## Project Structure
```
.
├── app.py
├── cifar10_model.h5
├── requirements.txt
├── static
│   └── uploads
│       ├── image1.jpg
│       ├── image2.jpg
│       └── ...
├── templates
│   ├── index.html
│   └── result.html
```

## How to Use
1. **Open the Web App**
   - Navigate to the gallery where all the uploaded images are displayed.

2. **Classify an Image**
   - Click on any image in the gallery to view its predicted class.

3. **View Results**
   - The classified result will display the uploaded image alongside its predicted class.

## Sample Output
**Gallery View:**
```
[ Image1 ]  [ Image2 ]  [ Image3 ]
[ Image4 ]  [ Image5 ]  [ Image6 ]
```

**Result Page Example:**
```
Prediction: Dog
```

## Troubleshooting
If you face issues while running the app:
- Ensure `cifar10_model.h5` is correctly located in the root directory.
- Verify that `static/uploads/` contains valid image files.
- Use `pip show tensorflow` to confirm TensorFlow is installed.
