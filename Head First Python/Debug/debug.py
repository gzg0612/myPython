import datetime
from ctypes import *
def MessageBox(title_string, content_string):
    user32 = windll.LoadLibrary('user32.dll')               # 加载动态链接库
    user32.MessageBoxW(0, content_string, title_string, 0)   # 调用MessageBoxA函数
def OutPutLog(FullfilePath, log):
    timestamp1 = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day)
    timestamp2 = str(datetime.datetime.now().hour) + ':' + str(datetime.datetime.now().minute) + ':' + str(datetime.datetime.now().second) + ':' + str(datetime.datetime.now().microsecond / 1000)
    timestamp = timestamp1 + ' ' + timestamp2
    with open(FullfilePath,'a') as f:
        print(timestamp + ' ' + str(log), file=f)