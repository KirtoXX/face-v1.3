# Face Beautiful Rating System
This is a simlpe Deep Learning Applecation on B/S architecture.<p>
  
## library:
1.Keras2 <p>
2.TensorFlow 1.4<p>
3.Flask<p>
4.Scipy<p>
![](https://github.com/KirtoXX/face-v1.3/blob/master/reference/%E6%95%B0%E6%8D%AE%E6%B5%81%E5%9B%BE.png)<p>

# How to Run
You can run the System both on local or Android Client(need serving.)<p>
url of weight: https://pan.baidu.com/s/1pKQvn3H, copy the weight to  ./weight/ <p> 
## local
1.pip install or library we need.<p>
2.cd the img to the ./iamge/ <p>
3.python predict.py xxx.jpg<p>

## Android Client
![](https://github.com/KirtoXX/face-v1.3/blob/master/reference/%E6%95%B0%E6%8D%AE%E6%B5%81%E5%9B%BEsystem.png)

### Start the serving:
python Flask_serving.py --port=<your_ip>  --port=<80> <p>

### fix the Android client
1 down load the Android client，url：<p>
Open the android client by ide and fix the host on java/ljw/myapi  <p>
![](https://github.com/KirtoXX/face-v1.3/blob/master/reference/client.png)
  
