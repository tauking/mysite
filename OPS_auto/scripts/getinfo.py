import os
#import psutil

def get_cpu_count():
    cpu_count = os.cpu_count()
    return cpu_count

def getMemCpu():
    '''
    data = psutil.virtual_memory()
    total = data.total  # 总内存,单位为byte
    free = data.available  # 可以内存
    memory = int(round(data.percent))
    cpu = psutil.cpu_percent(interval=1)
    '''
    return "hello"

