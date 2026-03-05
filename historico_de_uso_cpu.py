import psutil, time
while 1:
 f=open('cpu_log.txt','a')
 f.write(f"{time.ctime()} - CPU: {psutil.cpu_percent()}%\n")
 f.close()
 time.sleep(5)