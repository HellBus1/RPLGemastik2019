import warnings
warnings.simplefilter("ignore", UserWarning)
import pickle
from keras.applications.mobilenet import MobileNet, preprocess_input
from keras.models import Model
from keras.layers import Input
from keras.preprocessing import image
import numpy as np
import sys
base_path = 'A:\\proyekGemastik\\Repository\\tensorflow\\'
base_model = MobileNet(include_top=False, weights="imagenet",
                       input_tensor=Input(shape=(224, 224, 3)),
                       input_shape=(224, 224, 3))
output = base_model.output
model = Model(inputs=base_model.input, outputs=output)
image_size = (224, 224)

img = image.load_img(sys.argv[1], target_size=image_size)
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
feature = model.predict(x)
flat = feature.flatten()  ### double flatten dg diatas
load_pickle_file = open(base_path + 'mobilenet\\classifier.pickle', 'rb')
loaded_model = pickle.load(load_pickle_file, encoding='latin1')
predicted = loaded_model.predict([flat])

pkl_file = open(base_path + 'mobilenet\\encoder.pickle', 'rb')
lab = pickle.load(pkl_file)
pkl_file.close()
predictions_test = lab.inverse_transform(predicted)
print(predictions_test[0])

result_file = open('A:\\proyekGemastik\\Repository\\tensorflow\\result.txt', 'w+')
result_file.write(predictions_test[0])
result_file.close()