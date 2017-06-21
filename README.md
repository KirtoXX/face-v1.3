# face-v1.3
颜值评测系统
  
基于opencv3 TensorFlow1.2 keras2编写
  
后期填坑吧
  
预装工具 opencv，tensorflow，keras，anaconda3 
语言环境 python3.5  
  
权重文件地址：  
https://pan.baidu.com/s/1pKQvn3H  
存放地址：weight/  
  
本地用法：  
1.用于预测的人脸图片存储在 image/目录下  
2.temp/目录下存放框住人脸后的图片    
3.人脸检测器分别存贮在haarcascades/ 和 haarcascades_cuda/ 目录下，可按需求更换  
4. weight目录下存储网络权重，可以更换，但是网络结构不可更换  
5.用法 cd到该目录下，将图片存放到image/目录下 命令行下输入 python predict.py xxx.jpg 最后一行输出得分  
  
服务器版本：  
实现了两种版本的，一种FLASK的，一种基于socket的，FLask的最完善  
  
线上模型：  
1.cd到工程文件下  
2.python Flask_serving.py --ip=127.0.0.1 --port=9999  //根据需求更改  
3.Android 客户端实现访问   
3.1 Android 客户端地址 http://pan.baidu.com/s/1pKXMJY7   
3.2 修改java/myapi 下的host -.- 用Android stdio 打开  

//-------------更新用----------------      
1.支持png图片  
2.精度提升至94%  
