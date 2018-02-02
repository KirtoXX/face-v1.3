# Face Beautiful Rating System
This is a simlpe Deep Learning Applecation on C/S architecture.<p>
  
## library:
1.Keras2 <p>
2.TensorFlow 1.4<p>
3.Flask<p>
4.Scipy<p>
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
python Flask_serving.py --port=<your_ip>  --port=<80> <p>

### 2.fix the Android client
1 Download the Android client，url：<p>
2.Open the Android client by Android stdio,ix the <host> on java/ljw/myapi(make sure keep same with Flask_serving)   <p>
3.Install the Android client on your Smart Phone,enjoy it!<p>
![](https://github.com/KirtoXX/face-v1.3/blob/master/reference/client.png)
  
  
# Detel of module
### 1.face detection module：

### 2.Rating module：

