from ultralytics import YOLO
import yaml
import os
import cv2

def predict_on_image(model, image_path):
    # Predict on a single image
    results = model.predict(image_path,save_txt=True,save_conf=True,show=True)
    
        
    

def predict_on_webcam(model):
    # Predict using webcam
    model.predict(source="0",save_txt=True, show=True)

def main():
    model_path = "/Users/sandeepanghosh/Downloads/Food_CNN/last.pt"
    model = YOLO(model_path)

    print("Choose an option:")
    print("1. Predict on an image")
    print("2. Predict using webcam")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        image_path = input("Enter the path to the image: ")
        predict_on_image(model, image_path)
    elif choice == '2':
        predict_on_webcam(model)
    else:
        print("Invalid choice. Please choose either 1 or 2.")

if __name__ == "__main__":
    main()
