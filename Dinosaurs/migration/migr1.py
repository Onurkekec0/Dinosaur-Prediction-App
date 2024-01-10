import tensorflow as tf
import os
from keras.utils import img_to_array , load_img
import numpy as np
import cv2

class ModelKararS:
    def __init__(self):
        pass
    def modelKarar(self,file_path):
        model = tf.keras.models.load_model(r'C:\Users\Hp\Desktop\Jupyter\Dinosaurs\Dinosaurs\migration\model.h5')
        print(model.summary())

        batchSize = 32

        # categories
        source_folder = r'C:\Users\Hp\Desktop\Jupyter\archive'
        categories = os.listdir(source_folder)
        categories.sort()
        print(categories)

        numOfClasses = len(categories)
        print("Number of categories :")
        print(numOfClasses)

        def prepareImage(pathForImage):
            image = load_img(pathForImage, target_size=(256, 256))
            imgResult = img_to_array(image)
            imgResult = np.expand_dims(imgResult, axis=0)
            imgResult = imgResult / 255.
            return imgResult

        # run the prediction
        testImagPath = file_path
        # testImagPath = "TensorFlowProjects/Dinosaurs-Classification/test2_Triceratops.jpg"

        imageForModel = prepareImage(testImagPath)

        resultArray = model.predict(imageForModel, batch_size=batchSize, verbose=1)
        answers = np.argmax(resultArray, axis=1)
        # print(answers[0])

        text = categories[answers[0]]
        print("Predicted : " + text)
        return text

