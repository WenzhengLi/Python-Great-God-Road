import time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
time.sleep(1)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
time.sleep(1)
# 默认当前时间 time.loacltime()
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
