from flask import Flask, render_template,request
from DL_model import Are_U_Beatutifut
from socket_util import *
import tensorflow as tf

#-------init Flask app--------
app = Flask(__name__)

#-------init tensorflow ps--------
flags = tf.app.flags
flags.DEFINE_string("ip",False,"define ip")
flags.DEFINE_integer("port",9999,"define port")
FLAGS = flags.FLAGS

#--------init DL_model---------
global model
model = Are_U_Beatutifut()
model.build()

#--------define FLASK func--------
@app.route('/file', methods=['POST','GET'])
def update_file():

    save_path = "image/"

    if request.method == 'POST':
        #save file
        f = request.files['userfile']
        image_path = save_path+f.filename
        f.save(image_path)

        print(image_path)

        #inference
        result = model.rating(image_path)
        if result[0] == 1:
            score = result[2]
            temp = float_to_str(score)
        else:
            temp = bytes("no face",encoding="utf8")

    return temp


#-------define main--------
def main(_):
    ip = FLAGS.ip
    port = FLAGS.port
    app.run(host=ip,port=port)



if __name__ == '__main__':
    tf.app.run()


