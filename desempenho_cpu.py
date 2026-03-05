import psutil, time
while 1:
 t, p = psutil.cpu_percent(), psutil.cpu_percent(percpu=True)
 print(f"Total: {t}%\n" + " | ".join(f"N{i}: {v}%" for i, v in enumerate(p)))
 time.sleep(1)