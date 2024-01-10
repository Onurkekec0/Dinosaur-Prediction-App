# Dinosaur-Prediction-App

This project involves the development of a dinosaur classification model using Convolutional Neural Networks (CNN). The model has been integrated into a web application where users can explore and test their knowledge of various dinosaur species.

## Technologies Used

- **CNN Model Parameters:**
  - Number of Filters: 32
  - Filter Size: 3x3
  - Pooling Size: 2x2

- **Activation Functions:**
  - Output Layer: Softmax
  - Intermediate Layers: ReLU

- **Technologies:**
  - Python
  - Django
  - HTML, CSS, JavaScript

## Dataset

The dinosaur images and names used in this project were scraped from the [Natural History Museum's Dino Directory](https://www.nhm.ac.uk/discover/dino-directory) website.

## Test Application

To enhance user engagement, a test application has been incorporated, allowing users to assess their knowledge of dinosaurs.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Onurkekec0/Dinosaur-Prediction-App.git
   cd Dinosaur-Prediction-App

2. Set up the Django environment:
   ```bash
   pip install -r requirements.txt
   python manage.py migrate

4. Run the development server:
   ```bash
   python manage.py runserver
  
Visit http://localhost:8000 in your web browser to explore the Dinosaur Classification web application.



