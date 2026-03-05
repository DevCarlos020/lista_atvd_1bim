import psutil, time
L=float(input('%:'))
while 1:
 u=psutil.virtual_memory().percent
 print(f"Uso:{u}%")
 if u>L:print("ALERTA: MEMORIA CHEIA!")
 time.sleep(2)