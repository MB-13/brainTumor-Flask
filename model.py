import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing.image import load_img,img_to_array
import PIL


def load_my_model(model_path):
    model = load_model(model_path)
    return model

def predict(img_path,model):
    class_names = ['glioma tumor','meningioma tumor','no tumor','pituitary tumor']
    img = load_img(img_path,target_size=(224,224))
    image = img_to_array(img)
    image = image.reshape((1,image.shape[0],image.shape[1],image.shape[2]))
    out = model.predict(image)
    out = np.argmax(out)
    result = class_names[out]
    return result