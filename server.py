from flask import Flask, request
import numpy as np
from PIL import Image
from keras.preprocessing import image
from tensorflow import keras
import datetime

model = keras.models.load_model('rps.h5')


app = Flask(__name__)
r={0:'Paper',
     1:'Rock',
     2:'Scissors'}

@app.route("/send_file", methods=['POST'])
def send_file():

    img = Image.open(request.files['file'])
    img.thumbnail((150, 150), Image.ANTIALIAS)
    x = image.img_to_array(img)
    x=x[:, :, :3]
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    classes = r[np.argmax(classes[0])]
    now = datetime.datetime.now()
    rtime = now.strftime("%Y-%b-%d %H:%M:%S")

    return f'Rock, Paper and Scissors image classification server.\nLeila Vajed\nThe image you’ve submitted is classified as a: {classes}.\n{rtime}\n'
if __name__=="__main__":
    app.run(port=5000)