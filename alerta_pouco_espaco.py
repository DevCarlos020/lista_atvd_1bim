import psutil
L=float(input('%:'))
for p in psutil.disk_partitions():
 if 'snap' in p.mountpoint: continue
 u=psutil.disk_usage(p.mountpoint)
 if u.percent>(100-L):print(f"CRITICO: {p.mountpoint} ({u.percent}%)")