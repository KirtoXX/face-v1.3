from socket_util import *
from DL_model import Are_U_Beatutifut
import tensorflow as tf
from struct import pack

def main(argv=None):

    #-------socket_init-------
    s = socket_init()

    #-------deep_learning_system_init-------
    AI = Are_U_Beatutifut()
    AI.build()
    print('Start Serving')

    #--------start_serving-------
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        data = conn.recv(1024)
        if not data:
            break
        else:
            try:
                image_name = receive_image(data=data,conn=conn)
                result = AI.rating(image_name)
                if result[0]==1:
                    score = result[2]
                    temp = float_to_str(score)
                    conn.send(temp)
                else:
                    score = -1
                    temp = int_to_str(score)
                    conn.send(temp)
                print(result)
            except:
                print('error')
        conn.close()


if __name__ == '__main__':
    main()
