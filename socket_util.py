import socket

def getipaddrs(hostname):  # 只是为了显示IP，仅仅测试一下
    result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
    return [x[4][0] for x in result]

def receive_image(data,conn):
    # ------recive_name------
    filename = str(data, encoding="utf-8")
    print('file name:' + filename)
    filepath = "image/" + filename
    f = open(filepath, 'wb')
    # -------recive_file------
    while True:
        image = conn.recv(1024)
        if image == b'EOF':
            f.close()
            break
        else:
            f.write(image)
    print('recive finish!')
    return filename

def socket_init():

    host = '127.0.0.1'  # 为空代表为本地host
    port = 9999  # Arbitrary non-privileged port

    hostname = socket.gethostname()
    hostip = getipaddrs(hostname)
    print('host ip:', hostip)  # 应该显示为：127.0.0.1
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(4)
    return s


def float_to_str(a):
    temp = "%f"%(a)
    temp = bytes(temp, encoding = "utf8")
    return temp

def int_to_str(a):
    temp = "%d"%(a)
    temp = bytes(temp, encoding="utf8")
    return temp


