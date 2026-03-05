import psutil, time
while True:
 m = psutil.virtual_memory()
 print(f"T:{m.total/1024**2:.0f} U:{m.used/1024**2:.0f} L:{m.available/1024**2:.0f}MB ({m.available*100/m.total:.1f}%)")
 time.sleep(2)
