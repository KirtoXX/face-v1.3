# Face Beautiful Rating System
This is a simlpe Deep Learning Applecation on C/S architecture.<p>
  
## library:
1.Keras2 <p>
2.TensorFlow 1.4<p>
3.Flask<p>
4.Scipy<p>
5.OpenCV 3<p>
![](https://github.com/KirtoXX/face-v1.3/blob/master/reference/%E6%95%B0%E6%8D%AE%E6%B5%81%E5%9B%BE.png)<p>

# How to Run
You can run the System both on local or Android Client(need serving.)<p>
url of weight: https://pan.baidu.com/s/1pKQvn3H, copy the weight to  ./weight/ <p><p>

## local
1.pip install or library we need.<p>
2.copy the img to the ./iamge/ <p>
3.python predict.py xxx.jpg<p>

## Android Client
![](https://github.com/KirtoXX/face-v1.3/blob/master/reference/%E6%95%B0%E6%8D%AE%E6%B5%81%E5%9B%BEsystem.png)

### 1.Start the serving:
python Flask_serving.py --ip=<your_ip>  --port=<80> <p>

### 2.fix the Android client
1 Download the Android client，url：<p>
2.Open the Android client by Android stdio,fix the host on java/ljw/myapi  <p>
    (make sure keep same with Flask_serving)   <p>
3.Install the Android client on your Smart Phone,enjoy it!<p>
![](https://github.com/KirtoXX/face-v1.3/blob/master/reference/client.png)
  
  
# Detel of module
### 1.face detection module：
The module saved on haarcascades/ and haarcascades_cuda/.<p>
The face detection API implement by OpenCV 3.
  
### 2.Rating module：
(1).The Deep neural network was trained on SCUT Face Data.<p>
  finaly accuracy：97.2% <p> 
  url of data：www.hcii-lab.net/data/SCUT-FBP/CN/introduce.html <p>
(2).Architecture of CNNs(vgg): <p>
  ![](https://github.com/KirtoXX/face-v1.3/blob/master/reference/1709146-203d21703e0c7ac9.png)<p>

