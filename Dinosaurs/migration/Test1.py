from tensorflow import keras
import os
import cv2
import numpy as np

# Modeli yükle
class main():
    def ModelKarar(self,foto):
        model = keras.models.load_model(r'/Dinosaurs/model.h5')
        images = []
        labels = []

        # Görüntüleri ve etiketleri doldur
        for filename in os.listdir('../../Media'):
            if filename.endswith('.jpeg' or '.jpg' or '.png'):
                image_path = os.path.join('../../Media', filename)
                # Görüntüyü yükleyin
                image = cv2.imread(image_path)
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                resized_image = cv2.resize(gray_image, (256, 256))
                normalized_image = resized_image / 255.0
                images.append(normalized_image)

        # Görüntüleri Numpy dizisine dönüştür
        images = np.array(images)

        # Görüntüleri model üzerinde tahmin et
        predictions = model.predict(images)

        predicted_labels = np.argmax(predictions, axis=1)

        # Tahmin edilen etiketleri yazdır
        for i, prediction in enumerate(predicted_labels):
            print(f"Dosya {i+1} için tahmin: {prediction}")
